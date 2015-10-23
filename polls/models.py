from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
# Create your models here.

# Mira ponle mas claro a este modelo
class xxxxxxx(models.Model):
    

    question_text = models.CharField(max_length=20)
    pub_date = models.DateTimeField('date published')


class zzzzzzzz(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=20)
    votes = models.IntegerField(default=0)


class Salario(models.Model):
    cantidad = models.CharField(max_length=200)
    bono = models.CharField(max_length=200)
