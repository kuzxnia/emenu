from factory import Faker
from factory.django import DjangoModelFactory

from emenu.models import Menu


class MenuFactory(DjangoModelFactory):

    name = Faker("name")
    description = Faker("description")

    class Meta:
        model = Menu
