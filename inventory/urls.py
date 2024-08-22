from django.urls import path
from .views import ItemDetailView, CreateItem, DeleteItem, UpdateItem

urlpatterns = [
    path("item/detail/<int:pk>/", ItemDetailView.as_view(), name="item_detail_view"),
    path("create/item/", CreateItem.as_view(), name="create_item"),
    path("delete/item/<int:pk>", DeleteItem.as_view(), name="delete_item"),
    path("update/item/<int:pk>", UpdateItem.as_view(), name="update_item"),
]
