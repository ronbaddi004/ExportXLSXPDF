from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import related

# Create your models here.
User = get_user_model()


class Employee(models.Model):
    first_name                  = models.CharField(max_length=120)
    last_name                   = models.CharField(max_length=120)
    id_number                   = models.CharField(max_length=30)
    phone_number                = models.CharField(max_length=15)
    email                       = models.EmailField(unique=True)
    job_title                   = models.CharField(max_length=100)

    created_by                  = models.ForeignKey(User, on_delete=models.PROTECT, related_name="employees")

    def __str__(self):

        return f"{self.first_name} {self.last_name}"
