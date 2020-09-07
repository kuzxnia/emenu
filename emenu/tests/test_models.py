import pytest

from emenu.models import Menu

pytestmark = pytest.mark.django_db


def test_menu_get_absolute_url(menu: Menu):
    assert menu.get_absolute_url() == f"/menus/{menu.id}/"
