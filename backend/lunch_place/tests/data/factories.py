import factory
from faker import Faker
from lunch_app.models import Restaurant, Employe, Menu, Vote
from tests.data.mock.menu import MENU_DATA


fake = Faker()


class RestaurantFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Restaurant

    name = factory.Faker("name")
    address = fake.address()
    phone_number = f"{fake.country_calling_code()} {fake.phone_number()}"[:10]


class EmployeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Employe

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    restaurant = factory.SubFactory(RestaurantFactory)
    menu = MENU_DATA


class VoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vote

    menu = factory.SubFactory(MenuFactory)
    voted_by = factory.SubFactory(EmployeFactory)
