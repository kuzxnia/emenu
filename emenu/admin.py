from django.contrib import admin
from django.utils.html import mark_safe
from django.utils.translation import gettext_lazy as _

from .forms import DishForm, MenuForm
from .models import Dish, Menu


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    form = DishForm
    fields = ("name", "description", "price", "prep_time", "is_vegetarian", "image")
    list_display = (
        "name",
        "description",
        "price",
        "prep_time",
        "is_vegetarian",
        "admin_thumbnail",
    )
    readonly_fields = ("admin_thumbnail",)

    def admin_thumbnail(self, obj):
        return mark_safe(
            u'<img src="%s" width="120" height="auto" />' % obj.image.url
            if obj.image
            else None
        )

    admin_thumbnail.short_description = _("Image")
    admin_thumbnail.allow_tags = True


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    form = MenuForm
    list_display = ("name", "description")
