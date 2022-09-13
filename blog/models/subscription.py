from django.forms import EmailField

from django.db import models


class NewsLetter(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
