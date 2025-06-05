from django.db import models

class Category(models.Model):

    category_name = models.CharField(max_length=200)

    def __str__(self):

        return self.category_name

class Product(models.Model):

    # category_reference = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    category_reference = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length = 200, null=True)
    product_code = models.CharField(max_length = 200, null=True)
    price = models.FloatField(default=0)
    gst = models.IntegerField(default=0)
    food_product = models.BooleanField(default=False)
    picture = models.ImageField(null=True, upload_to='imgaes/')

    def __str__(self):

        return self.product_name