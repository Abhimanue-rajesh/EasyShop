from django.db import models
from django.contrib.auth.models import User


class ItemCategory(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    category = models.ForeignKey(ItemCategory, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(
        upload_to="item_images",
        blank=True,
        default="item_images/empty_image.jpg",
    )

    def __str__(self):
        return self.name


class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart for {self.user.username}"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.name}"

    @property
    def total_price(self):
        return self.quantity * self.item.price
