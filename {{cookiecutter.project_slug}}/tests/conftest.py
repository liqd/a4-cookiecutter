import factory
import pytest
from django.urls.base import get_resolver
from pytest_factoryboy import register
from rest_framework.test import APIClient

from adhocracy4.test import factories as a4_factories
from adhocracy4.test.factories.maps import AreaSettingsFactory
from adhocracy4.test.helpers import patch_background_task_decorator

from . import factories


register(factories.UserFactory)
register(factories.UserFactory, 'user2')
register(factories.AdminFactory, 'admin')
register(factories.OrganisationFactory)

register(factories.PhaseFactory)
register(factories.PhaseContentFactory)
register(factories.CategoryFactory)
register(factories.CommentFactory)
register(factories.RatingFactory)

register(a4_factories.ProjectFactory)
register(a4_factories.ModuleFactory)
register(AreaSettingsFactory)


@pytest.fixture
def apiclient():
    return APIClient()


@pytest.fixture
def ImagePNG():
    return factory.django.ImageField(width=1400, height=1400, format='PNG')
