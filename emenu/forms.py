from django.core.exceptions import ValidationError
from django.forms import ModelChoiceField, ModelForm
from django.utils.translation import gettext_lazy as _

from emenu.models import Dish, Menu


class DishForm(ModelForm):
    menu = ModelChoiceField(required=True, queryset=Menu.objects.all())

    class Meta:
        model = Dish
        fields = ["name", "description", "price", "prep_time", "is_vegetarian", "image"]


class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = ["name", "description"]

    def clean_name(self):
        name = self.cleaned_data["name"]

        try:
            Menu.objects.get(name=name)
        except Menu.DoesNotExist:
            return name

        raise ValidationError(_("This name has already been taken."))
