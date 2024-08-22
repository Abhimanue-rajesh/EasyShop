from django.urls import path
from .views import Home, add_to_cart, view_cart, remove_from_cart


urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("add-to-cart/<int:pk>/", add_to_cart, name="add_to_cart"),
    path("cart/", view_cart, name="view_cart"),
    path('remove-from-cart/<int:pk>/', remove_from_cart, name='remove_from_cart'),
]
