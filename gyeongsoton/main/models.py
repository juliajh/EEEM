from django.db import models
from django.conf import settings

# Create your models here.


class newterm(models.Model):
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    non_answer = models.CharField(max_length=100)

class communityText(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=500)
    like = models.IntegerField()
    dis_like = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')
    title=models.CharField(max_length=30,default='')

    def __str__(self):
        return self.text[:50]+"..."


class communityComment(models.Model):
    date = models.DateTimeField()
    communitytext = models.ForeignKey(
        communityText, on_delete=models.CASCADE, default='')
    like = models.IntegerField()
    dis_like = models.IntegerField()
    text = models.CharField(max_length=300)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='')


class manner(models.Model):
    text = models.CharField(max_length=20)
    like = models.IntegerField()
    dis_like = models.IntegerField()
    hashtag_me = models.CharField(max_length=20)
    hashtag_you = models.CharField(max_length=20)
    hashtag_situation = models.CharField(max_length=500)
