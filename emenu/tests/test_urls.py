import pytest
from django.urls import resolve, reverse

from emenu.models import Menu

pytestmark = pytest.mark.django_db


def test_detail(menu: Menu):
    assert reverse("menu:detail", kwargs={"pk": menu.id}) == f"/menus/{menu.id}/"
    assert resolve(f"/menus/{menu.id}/").view_name == "menu:detail"


def test_list():
    assert reverse("menu:list") == "/"
    assert resolve("/").view_name == "menu:list"
