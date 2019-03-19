import pytest
from django.core.urlresolvers import reverse

from adhocracy4.test.helpers import redirect_target
from apps.mapideas import models
from apps.mapideas import phases
from tests.helpers import freeze_phase
from tests.helpers import setup_phase


@pytest.mark.django_db
def test_creator_can_update_during_active_phase(client, phase_factory,
                                                map_idea_factory,
                                                category_factory,
                                                area_settings_factory):
    phase, module, project, mapidea = setup_phase(
        phase_factory, map_idea_factory, phases.IssuePhase)
    category = category_factory(module=module)
    area_settings_factory(module=module)
    user = mapidea.creator
    url = reverse(
        'mapidea-update',
        kwargs={
            'slug': mapidea.slug
        })
    with freeze_phase(phase):
        client.login(username=user.email, password='password')
        data = {
            'name': 'Another MapIdea',
            'description': 'changed description',
            'category': category.pk,
            'point': (0, 1),
            'point_label': 'somewhere else'
        }
        response = client.post(url, data)
        assert redirect_target(response) == 'mapidea-detail'
        assert response.status_code == 302
        updated_mapidea = models.MapIdea.objects.get(id=mapidea.pk)
        assert updated_mapidea.description == 'changed description'


@pytest.mark.django_db
def test_creator_cannot_update_in_wrong_phase(client, phase_factory,
                                              map_idea_factory,
                                              category_factory):
    phase, module, project, mapidea = setup_phase(
        phase_factory, map_idea_factory, phases.RatingPhase)
    category = category_factory(module=module)
    user = mapidea.creator
    assert user not in project.moderators.all()
    url = reverse(
        'mapidea-update',
        kwargs={
            'slug': mapidea.slug
        })
    with freeze_phase(phase):
        client.login(username=user.email, password='password')
        data = {
            'name': 'Another MapIdea',
            'description': 'changed description',
            'category': category.pk,
            'point': (0, 1),
            'point_label': 'somewhere else'
        }
        response = client.post(url, data)
        assert response.status_code == 403


@pytest.mark.django_db
def test_moderator_can_update_during_wrong_phase(client, phase_factory,
                                                 map_idea_factory,
                                                 category_factory,
                                                 area_settings_factory):
    phase, module, project, mapidea = setup_phase(
        phase_factory, map_idea_factory, phases.RatingPhase)
    category = category_factory(module=module)
    area_settings_factory(module=module)
    user = mapidea.creator
    moderator = project.moderators.first()
    assert moderator is not user
    url = reverse(
        'mapidea-update',
        kwargs={
            'slug': mapidea.slug
        })
    with freeze_phase(phase):
        client.login(username=moderator.email, password='password')
        data = {
            'name': 'Another MapIdea',
            'description': 'changed description',
            'category': category.pk,
            'point': (0, 1),
            'point_label': 'somewhere else'
        }
        response = client.post(url, data)
        assert redirect_target(response) == 'mapidea-detail'
        assert response.status_code == 302
        updated_mapidea = models.MapIdea.objects.get(id=mapidea.pk)
        assert updated_mapidea.description == 'changed description'


@pytest.mark.django_db
def test_creator_cannot_update(client, map_idea_factory):
    mapidea = map_idea_factory()
    user = mapidea.creator
    assert user not in mapidea.module.project.moderators.all()
    url = reverse(
        'mapidea-update',
        kwargs={
            'slug': mapidea.slug
        })
    client.login(username=user.email, password='password')
    data = {
        'name': 'Another MapIdea',
        'description': 'changed description',
        'category': category.pk,
        'point': (0, 1),
        'point_label': 'somewhere else'
    }
    response = client.post(url, data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_moderators_can_always_update(client, map_idea_factory):
    mapidea = map_idea_factory()
    moderator = mapidea.module.project.moderators.first()
    assert moderator is not mapidea.creator
    url = reverse(
        'mapidea-update',
        kwargs={
            'slug': mapidea.slug
        })
    client.login(username=moderator.email, password='password')
    data = {
        'name': 'Another MapIdea',
        'description': 'changed description'
    }
    response = client.post(url, data)
    assert redirect_target(response) == 'mapidea-detail'
    assert response.status_code == 302
    updated_mapidea = models.MapIdea.objects.get(id=mapidea.pk)
    assert updated_mapidea.description == 'changed description'
