import datetime
from rest_framework import viewsets
from lunch_app.models import Restaurant, Employe, Menu, Vote
from authentication.mixins import StaffEditorPermissionMixin
from lunch_app.serializers import (
    RestaurantSerializer,
    EmployeSerializer,
    MenuSerializer,
    VoteSerializer,
)


class RestaurantViewSet(StaffEditorPermissionMixin, viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    lookup_field = "uuid"


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    lookup_field = "uuid"


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    lookup_field = "uuid"

    def get_queryset(self):
        query = None
        target_date = datetime.datetime.today().strftime("%Y-%m-%d")
        if self.kwargs.get("uuid", None):
            restaurant = Restaurant.objects.get(uuid=self.kwargs["uuid"])
            _query = self.queryset.filter(
                restaurant=restaurant, updated__date=target_date
            )
            query = _query if _query.prefetch_related().first().vote_count > 0 else None
        else:
            query = self.queryset.filter(updated__date=target_date)
        return query


class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer
    lookup_field = "uuid"
