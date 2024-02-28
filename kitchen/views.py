from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import generic

from kitchen.models import DishType, Dish, Cook


def index(request: HttpRequest) -> HttpResponse:
    num_dishes = Dish.objects.count()
    num_cooks = Cook.objects.count()
    num_dish_types = DishType.objects.count()
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1
    context = {
        "num_dishes": num_dishes,
        "num_cooks": num_cooks,
        "num_dish_types": num_dish_types,
        "num_visits": num_visits + 1,
    }
    return render(request, "kitchen/index.html", context)


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "kitchen/dish_types_list.html"
    context_object_name = "dish_type_list"


class CookListView(generic.ListView):
    model = Cook


class DishListView(generic.ListView):
    model = Dish
