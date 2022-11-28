import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from tests.data.mock.create_models import RESTAURANT_DATA
from tests.data.factories import (
    RestaurantFactory,
    EmployeFactory,
    MenuFactory,
    VoteFactory,
)


client = APIClient()


@pytest.mark.django_db
def test_get_restaurant(get_authorize_client):
    client = get_authorize_client
    RestaurantFactory()
    url = reverse("lunch_app:restaurants-view-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_employe(get_authorize_client):
    client = get_authorize_client
    EmployeFactory()
    url = reverse("lunch_app:employees-view-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_menu(get_authorize_client):
    client = get_authorize_client
    MenuFactory()
    url = reverse("lunch_app:menus-view-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_vote(get_authorize_client):
    client = get_authorize_client
    VoteFactory()
    url = reverse("lunch_app:votes-view-list")
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_restaurant(get_authorize_client):
    client = get_authorize_client
    restaurant_data = RESTAURANT_DATA
    url = reverse("lunch_app:restaurants-view-list")
    response = client.post(url, data=restaurant_data)

    assert response.data["name"] == RESTAURANT_DATA["name"]
    assert response.data["address"] == RESTAURANT_DATA["address"]
    assert response.data["phone_number"] == RESTAURANT_DATA["phone_number"]
    assert status.HTTP_201_CREATED == response.status_code
    assert isinstance(response.data, dict)
