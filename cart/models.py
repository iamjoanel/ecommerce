from django.db import models
from catalog.models import Product
import random


class CartItem(models.Model):
    cart_id = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField(default=1)
    product = models.ForeignKey('catalog.Product', unique=False)

    class Meta:
        db_table = 'cart_items'
        ordering = ['date_added']

    def total(self):
        return self.quantity * self.product.price

    def name(self):
        return self.name

    def price(self):
        return self.product.price

    def get_absolute_url(self):
        return self.product.get_absolute_url()

    def augment_quantity(self, quantity):
        self.quantity = self.quantity + int(quantity)
        self.save()

    def _generate_cart_id():
        cart_id = ''
        characters = 'ABCDEFGHIJKLMNOPQRQSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()'
        cart_id_length = 50
        for y in range(cart_id_length):
            cart_id += characters[random.randint(0, len(characters)-1)]
        return cart_id

    def _cart_id(request):
        if 'cart_id' in request.session:
            request.session['cart_id'] = _generate_cart_id()
        return request.session['cart_id']