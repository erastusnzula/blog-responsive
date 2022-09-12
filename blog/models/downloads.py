from django.db import models

class Download(models.Model):
    filename = models.CharField(max_length=255)
    mobile = models.FileField(upload_to='images/mobile', null=True, blank=True)
    windows = models.FileField(upload_to='images/windows', null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.filename
    
    class Meta:
        ordering = ['-added_on']