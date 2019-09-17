from django.db import models
from django.conf import settings
# Create your models here.


class Checkout_model(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    street = models.TextField()
    zipcode = models.IntegerField(default=True,max_length=5)


    def __str__(self):
        return self.first_name
