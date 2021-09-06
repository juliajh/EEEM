from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    sex = models.IntegerField(default=0)  # 남자 0, 여자 1
    age = models.IntegerField(default=0)
