import factory

from tests.factories import UserFactory


class OrganisationFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = '{{ cookiecutter.project_app_prefix }}_organisations.Organisation'
        django_get_or_create = ('name',)

    name = factory.Faker('company')

    @factory.post_generation
    def initiators(self, create, extracted, **kwargs):
        if not extracted:
            user = UserFactory()
            self.initiators.add(user)
            return

        if extracted:
            for user in extracted:
                self.initiators.add(user)
