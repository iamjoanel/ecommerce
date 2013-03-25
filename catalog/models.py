from django.db import models

# Create your models here.


class Category(models.Model):
    name        = models.CharField(max_length=50)
    description = models.TextField()
    is_active   = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table            = 'categories'
        ordering            = ['name']
        verbose_name_plural = 'Categories'

    def __unicode__(self):
        return self.name


class Product(models.Model):
    name          = models.CharField(max_length=50, unique=True)
    price         = models.DecimalField(max_digits=9, decimal_places=2)
    old_price     = models.DecimalField(max_digits=9, decimal_places=2, blank=True, default=0.00)
    image         = models.CharField(max_length=50)
    is_active     = models.BooleanField(default=True)
    is_featured   = models.BooleanField(default=True)
    is_bestseller = models.BooleanField(default=False)
    quantity      = models.IntegerField()
    created_at    = models.DateTimeField(auto_now_add=True)
    update_at     = models.DateTimeField(auto_now=True)
    categories    = models.ManyToManyField(Category)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __unicode__(self):
        return self.name

    def sale_price(self):
        if self.old_price > self.price:
            return self.price
        else:
            return None
