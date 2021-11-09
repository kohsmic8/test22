from django.db import models
from django.contrib.auth.models import AbstractUser


class 아이디(AbstractUser):
    pass

class sale(models.Model):
    
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    person = models.ForeignKey("person", on_delete=models.CASCADE)

class person(models.Model):

    회원 = models.OneToOneField(아이디, on_delete=models.CASCADE)

    def __str__(self):
        return self.회원.email
