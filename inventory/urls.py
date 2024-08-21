from django.urls import path
from .views import ItemDetailView

urlpatterns = [
    path("item/detail/<int:pk>/", ItemDetailView.as_view(), name="item_detail_view"),
]
