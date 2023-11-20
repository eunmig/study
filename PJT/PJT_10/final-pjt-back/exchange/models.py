from django.db import models

# Create your models here.


class Exchange(models.Model):
    country = models.TextField()
    rate = models.FloatField()
    currency_name = models.TextField()
    korean_name = models.CharField(max_length=20, blank=True, null=True)