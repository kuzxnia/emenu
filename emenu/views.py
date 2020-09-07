from django.db.models import Count
from django.views.generic import DetailView, ListView

from .models import Menu


class MenuListView(ListView):
    context_object_name = "menu_list"
    queryset = (
        Menu.objects.filter(dishes__isnull=False)
        .annotate(dish_amount=Count("dishes"))
        .filter(dish_amount__gt=0)
    )


class MenuDetailView(DetailView):
    queryset = Menu.objects.prefetch_related("dishes")
