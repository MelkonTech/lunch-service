import factory
import pytest
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from faker import Faker
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

fake = Faker()
client = APIClient()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = make_password(fake.password())
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    is_staff = True
    is_superuser = True
    is_active = True


@pytest.mark.django_db
def get_authorization_client():
    user = UserFactory()
    token = Token.objects.create(user=user)
    client.force_authenticate(user=user, token=token)

    return client
