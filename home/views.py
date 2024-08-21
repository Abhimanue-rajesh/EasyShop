from django.views.generic import ListView
from inventory.models import Item


class Home(ListView):
    model = Item
    template_name = "home/home.html"
    context_object_name = "all_items"
