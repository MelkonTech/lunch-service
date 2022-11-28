from django.urls import path, include
from lunch_app import views
from rest_framework import routers

app_name = "lunch_app"

main_router = routers.SimpleRouter()
main_router.register(
    "restaurants", views.RestaurantViewSet, basename="restaurants-view"
)
main_router.register("employees", views.EmployeesViewSet, basename="employees-view")
main_router.register("menus", views.MenuViewSet, basename="menus-view")
main_router.register("votes", views.VoteViewSet, basename="votes-view")

restaurant_router = routers.SimpleRouter()
restaurant_router.register(r"menu", views.MenuViewSet, basename="restaurant-menu-views")

menu_router = routers.SimpleRouter()
menu_router.register(r"vote", views.VoteViewSet, basename="vote-menu-views")


urlpatterns = [
    path(r"", include(main_router.urls)),
    path("restaurants/<str:uuid>/", include(restaurant_router.urls)),
    path("menu/<str:uuid>/", include(menu_router.urls)),
]
