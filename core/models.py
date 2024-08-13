from django.db import models
# from django.utils.translation import gettext_lazy as _


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()

    def __str__(self):
        return self.title
