from django.db import models


# Create your models here.
class UserForm(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    item = models.TextField()
    desc = models.TextField()
