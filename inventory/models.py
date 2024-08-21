from django.db import models


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
