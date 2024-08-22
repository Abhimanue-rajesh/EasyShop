from django.views.generic import ListView
from inventory.models import Item, Cart, CartItem
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


class Home(ListView):
    model = Item
    template_name = "home/home.html"
    context_object_name = "all_items"


@login_required
def add_to_cart(request, pk):
    item = get_object_or_404(Item, id=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect("view_cart")


@login_required
def view_cart(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_items = cart.items.all()
    total_amount = sum(item.total_price for item in cart_items)

    context = {
        "cart_items": cart_items,
        "total_amount": total_amount,
    }
    return render(request, "home/cart.html", context)


@login_required
def remove_from_cart(request, pk):
    cart_item = get_object_or_404(CartItem, id=pk, cart__user=request.user)
    cart_item.delete()
    return redirect("view_cart")
