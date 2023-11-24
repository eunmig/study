from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    salary = models.IntegerField(default=0)
    salary_level = models.IntegerField(default=0)
    financial_products = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        # Calculate salary_level based on the salary value
        if 0 <= self.salary < 2000:
            self.salary_level = 1
        elif 2000 <= self.salary < 4000:
            self.salary_level = 2
        elif 4000 <= self.salary < 5000:
            self.salary_level = 3
        elif 5000 <= self.salary < 8000:
            self.salary_level = 4
        else:
            self.salary_level = 5  # or any other default value

        super(User, self).save(*args, **kwargs)

class Car(models.Model):
    car_name = models.CharField(max_length=20, unique=True)
    price = models.IntegerField()
    year = models.TextField()
    salary_level = models.IntegerField()

    def save(self, *args, **kwargs):

        if 0 <= self.price < 2000:
            self.salary_level = 1
        elif 2000 <= self.price < 4000:
            self.salary_level = 2
        elif 4000 <= self.price < 5000:
            self.salary_level = 3
        elif 5000 <= self.price < 8000:
            self.salary_level = 4
        else:
            self.salary_level = 5

        super(Car, self).save(*args, **kwargs)