import os
import django
from tests.utils.authorization import get_authorization_client
import pytest

os.environ["DJANGO_SETTINGS_MODULE"] = "lunch_place.settings"

django.setup()


@pytest.fixture()
def get_authorize_client():
    client = get_authorization_client()

    return client
