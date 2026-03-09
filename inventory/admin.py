from django.contrib import admin
from unfold.admin import ModelAdmin

from inventory.models import Item, ItemCategory


@admin.register(Item)
class ItemsAdmin(ModelAdmin):
    pass


@admin.register(ItemCategory)
class ItemCategoriesAdmin(ModelAdmin):
    pass
