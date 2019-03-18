import pytest
from django.core.urlresolvers import reverse

from adhocracy4.test.helpers import redirect_target
from apps.mapideas import models
from apps.mapideas import phases
from tests.helpers import assert_template_response
from tests.helpers import freeze_phase


@pytest.mark.django_db
def test_anonymous_cannot_create_mapidea(client, phase_factory):
    phase = phase_factory(phase_content=phases.IssuePhase())
    module = phase.module
    url = reverse('mapidea-create',
                  kwargs={'slug': module.slug})
    with freeze_phase(phase):
        count = models.MapIdea.objects.all().count()
        assert count == 0
        response = client.get(url)
        assert response.status_code == 302
        assert redirect_target(response) == 'account_login'


@pytest.mark.django_db
def test_user_can_create_mapidea_during_active_phase(client, phase_factory, user,
                                                  category_factory):
    phase = phase_factory(phase_content=phases.IssuePhase())
    module = phase.module
    category = category_factory(module=module)
    url = reverse('mapidea-create',
                  kwargs={'slug': module.slug})

    with freeze_phase(phase):
        count = models.MapIdea.objects.all().count()
        assert count == 0
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert_template_response(
            response, '{{ cookiecutter.project_app_prefix }}_mapideas/mapidea_form.html')
        assert response.status_code == 200
        mapidea = {
            'name': 'MapIdea',
            'description': 'description',
            'category': category.pk,
            'point': (0, 0),
            'point_label': 'somewhere'
        }
        response = client.post(url, mapidea)
        assert response.status_code == 302
        assert redirect_target(response) == 'mapidea-detail'
        count = models.MapIdea.objects.all().count()
        assert count == 1


@pytest.mark.django_db
def test_user_cannot_create_mapidea_in_wrong_phase(client, phase_factory, user):
    phase = phase_factory(phase_content=phases.RatingPhase())
    module = phase.module
    url = reverse('mapidea-create',
                  kwargs={'slug': module.slug})
    with freeze_phase(phase):
        response = client.get(url)
        assert response.status_code == 302
        client.login(username=user.email, password='password')
        response = client.get(url)
        assert response.status_code == 403


@pytest.mark.django_db
def test_admin_can_create_mapidea_in_wrong_phase(client, phase_factory,
                                              category_factory, admin):
    phase = phase_factory(phase_content=phases.RatingPhase())
    module = phase.module
    category = category_factory(module=module)
    url = reverse('mapidea-create',
                  kwargs={'slug': module.slug})
    with freeze_phase(phase):
        client.login(username=admin.email, password='password')
        response = client.get(url)
        assert_template_response(
            response, '{{ cookiecutter.project_app_prefix }}_mapideas/mapidea_form.html')
        assert response.status_code == 200
        mapidea = {
            'name': 'MapIdea',
            'description': 'description',
            'category': category.pk,
            'point': (0, 0),
            'point_label': 'somewhere'
        }
        response = client.post(url, mapidea)
        assert response.status_code == 302
        assert redirect_target(response) == 'mapidea-detail'
        count = models.MapIdea.objects.all().count()
        assert count == 1
