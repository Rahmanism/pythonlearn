from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=560)