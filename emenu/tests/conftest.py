import pytest

from emenu.models import Menu
from emenu.tests.factories import MenuFactory


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def menu() -> Menu:
    return MenuFactory()
