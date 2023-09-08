from django.db import models

class Questions(models.Model):
    category = models.CharField(max_length=150)
    question = models.CharField(max_length=500)
    answer = models.CharField(max_length=100)
