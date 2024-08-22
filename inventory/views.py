from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Item
from .forms import CreateUpdateItem
from django.urls import reverse_lazy, reverse


class ItemDetailView(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "inventory/item_detail_view.html"
    context_object_name = "item"
    extra_context = {"page_title": "Item Detail"}


class CreateItem(LoginRequiredMixin, CreateView):
    model = Item
    form_class = CreateUpdateItem
    template_name = "inventory/create_update_item.html"
    success_url = reverse_lazy("home")


class DeleteItem(LoginRequiredMixin, DeleteView):
    model = Item
    template_name = "inventory/item_confirm_delete.html"
    success_url = reverse_lazy("home")


class UpdateItem(LoginRequiredMixin, UpdateView):
    model = Item
    form_class = CreateUpdateItem
    template_name = "inventory/create_update_item.html"

    def get_success_url(self):
        return reverse("item_detail_view", kwargs={"pk": self.object.id})
