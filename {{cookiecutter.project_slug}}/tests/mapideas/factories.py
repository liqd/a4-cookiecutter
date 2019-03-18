import factory

from adhocracy4.test import factories as a4_factories
from apps.mapideas import models as mapidea_models


class MapIdeaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = mapidea_models.MapIdea

    name = factory.Faker('sentence')
    description = '<script>alert("hello");</script>Description'
    creator = factory.SubFactory(a4_factories.USER_FACTORY)
    module = factory.SubFactory(a4_factories.ModuleFactory)
