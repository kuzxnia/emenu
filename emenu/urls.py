from django.urls import path

from . import views

app_name = "menus"
urlpatterns = [
    path("", views.MenuListView.as_view(), name="list"),
    path("menus/<slug:pk>/", views.MenuDetailView.as_view(), name="detail"),
]
