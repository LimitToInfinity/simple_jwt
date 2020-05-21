from django.db import models
from django.contrib.auth.models import User, AbstractUser

class Apple(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class User(AbstractUser):
    secret_agent = models.BooleanField(null=True)

    def __str__(self):
        return self.username