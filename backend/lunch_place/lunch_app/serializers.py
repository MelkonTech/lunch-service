from rest_framework import serializers
from lunch_app.models import Restaurant, Employe, Menu, Vote


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant

        fields = (
            "name",
            "address",
            "phone_number",
            "created",
            "updated",
            "description",
            "uuid",
        )


class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe

        fields = ("first_name", "last_name", "email", "name", "uuid")


class VoteSerializer(serializers.ModelSerializer):
    menu = serializers.SlugRelatedField(
        read_only=False, slug_field="uuid", queryset=Menu.objects.all()
    )

    class Meta:
        model = Vote
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    restaurant = serializers.SlugRelatedField(
        read_only=False, slug_field="uuid", queryset=Restaurant.objects.all()
    )

    class Meta:
        model = Menu

        fields = ("restaurant", "menu", "created", "updated", "vote_count", "uuid")
