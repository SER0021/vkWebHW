from django.contrib.auth.models import User
from django.db import models
from django.db.models import Count


# Create your models here.

class QuestionManager(models.Manager):
    def hotQuestions(self):
        return self.annotate(like_count=Count('like_question')).filter(like_count__gt=10)


class Answer(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey('Profile', on_delete=models.PROTECT)
    # like = models.ForeignKey('Like_answer', on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField()
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
    STATUS_CHOICES = (
        ('s', 'solution'),
        ('n', 'notsolution'),
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='n')
class Question(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=200)
    author = models.ForeignKey('Profile', on_delete=models.PROTECT)
    date = models.DateField()
    # like = models.ForeignKey('Like_question', on_delete=models.PROTECT, null=True, blank=True)
    tag = models.ForeignKey('Tag', on_delete=models.DO_NOTHING, null=True, blank=True)

    objects = QuestionManager()


class Profile(models.Model):
    email = models.CharField(max_length=40)
    nickname = models.CharField(max_length=20)
    # avatar = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)

class Like_question(models.Model):
    TYPES = (
        ('l', 'like'),
        ('d', 'dislike'),
    )
    type = models.CharField(max_length=1, choices=TYPES, default='l')
    user = models.ForeignKey('Profile', on_delete=models.DO_NOTHING)
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)
class Like_answer(models.Model):
    TYPES = (
        ('l', 'like'),
        ('d', 'dislike'),
    )
    type = models.CharField(max_length=1, choices=TYPES, default='l')
    user = models.ForeignKey('Profile', on_delete=models.DO_NOTHING)
    question = models.ForeignKey('Question', on_delete=models.DO_NOTHING)


class Tag(models.Model):
    title = models.CharField(max_length=30)