from django.db import models
from django.conf import settings

# Create your models here.


class newterm(models.Model):
    question = models.CharField()
    answer = models.CharField()
    non_answer = models.CharField()


class communityText(models.Model):
    date = models.DateTimeField()
    text = models.CharField(max_length=500)
    like = models.IntegerField()
    dis_like = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, default='')


class communityComment(models.Model):
    date = models.DateTimeField()
    communitytext = models.ForeignKey(
        communityText, on_delete=models.CASCADE, default='')
    like = models.IntegerField()
    dis_like = models.IntegerField()
    text = models.CharField(max_length=300)
    # 유저 fk 필요


class manner(models.Model):
    text = models.CharField(max_length=500)
    like = models.IntegerField()
    dis_like = models.IntegerField()
    hashtag_me = models.CharField()
    hashtag_you = models.CharField()
    hashtag_situation = models.CharField()


# 회원 클래스 생성 필요
