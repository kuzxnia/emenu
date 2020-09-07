from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    DecimalField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextField,
)
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CreateModMixin(Model):
    created_on = DateTimeField(default=timezone.now, editable=False)
    modified_on = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Menu(CreateModMixin):
    name = CharField(_("Name of Menu"), unique=True, blank=False, max_length=255)
    description = TextField(_("Description"), blank=True)

    def get_absolute_url(self):
        return reverse("menu:detail", kwargs={"pk": self.id})

    def __str__(self):
        return self.name


class Dish(CreateModMixin):
    name = CharField(_("Name of Menu"), unique=False, blank=False, max_length=255)
    description = TextField(_("Description"), blank=True)
    price = DecimalField(
        _("Price"),
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.01"))],
    )
    prep_time = IntegerField(_("Preparation time"))
    is_vegetarian = BooleanField(_("Is vegetarian dish"))
    image = ImageField(_("Dish image"), blank=True, null=True)
    menu = ForeignKey(Menu, on_delete=CASCADE, related_name="dishes")

    def __str__(self):
        return self.name
