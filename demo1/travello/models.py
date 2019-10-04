from django.db import models

# Create your models here.
class destination(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)