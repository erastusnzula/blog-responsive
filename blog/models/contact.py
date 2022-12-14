from django.db import models


class Contact(models.Model):
    email_address = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.email_address
