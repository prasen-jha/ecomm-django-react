from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, blank=False)
    slug = models.SlugField(max_length=200, blank=False)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    name = models.CharField(max_length=200,blank=False)
    slug = models.SlugField(max_length=200,blank=False)
    category = models.ForeignKey(Category,related_name='sub_categories',on_delete=models.CASCADE)
    description = models.TextField(blank=False)

    class Meta:
        verbose_name_plural='Sub-Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200,blank=False)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory,related_name='products',on_delete=models.CASCADE)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=3)
    is_available = models.BooleanField(default=True)
    is_on_discount = models.BooleanField(default=False)
    is_on_sale = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural='Products'


    def __str__(self):
        return self.name