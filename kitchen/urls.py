from django.urls import path
from kitchen.views import (
    index,
    DishTypeListView,
    CookListView,
    DishListView,
    CookDetailView,
)


urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypeListView.as_view(), name="dish-type-list"),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path("cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"),
    path("dishes/", DishListView.as_view(), name="dish-list"),
]

app_name = "kitchen"
