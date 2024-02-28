from django.urls import path

from kitchen.views import index, DishTypesListView, CooksListView

urlpatterns = [
    path("", index, name="index"),
    path("dish-types/", DishTypesListView.as_view(), name="dish-type-list"),
    path("cooks/", CooksListView.as_view(), name="cook-list"),
]

app_name = "kitchen"
