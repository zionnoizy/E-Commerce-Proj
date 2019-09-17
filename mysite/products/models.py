from django.db import models


# Create your models here.
class Category_model(models.Model):
    # COLOR_CHOICES = (
    # 	('RED', 'red'), ('BLUE', 'blue'), ('GREEN', 'green'), ('PURPLE', 'purple'),
    #     ('YELLOW', 'yellow'), ('BLACK', 'black'), ('WHITE', 'white'), ('GREY', 'grey'),
    #     ('VARITY', 'varity'), ('DARK GREEN', 'dark green'), ('NOT SPECIFY', 'not specify'),
    # )
    WHAT_CHOICES = (
    	('FOOD', 'food'), ('CLOTHES', 'clothes'), ('PLANT', 'plant'), ('DRINK', 'drink'),
        ('ELECTRONIC', 'electronic'), ('DECORATION', 'decoration'), ('UNKNOWN', 'unknown'), ('LEISURE', 'leisure'),
        ('GAME', 'game'), ('OTHERS', 'others'),
    )
    what_category = models.CharField(max_length=200, choices=WHAT_CHOICES, default='UNKNOWN')
    # color = models.CharField(max_length=200, choices=COLOR_CHOICES, default='NOT SPECIFY')

    def __str__(self):
        return "%s" % (self.what_category)

class Product_model(models.Model):
    name = models.CharField(max_length=110)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category_model, on_delete=models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="products_images", blank=True)
    stock = models.IntegerField(default=True)
    available = models.BooleanField(default=True)
    pdated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return "/products/%i/" % self.id

    def __str__(self):
        return self.name
