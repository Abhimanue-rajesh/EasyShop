from django.views.generic import DetailView
from .models import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = "inventory/item_detail_view.html"
    context_object_name = "item"
    extra_context = {"page_title": "Item Detail"}
