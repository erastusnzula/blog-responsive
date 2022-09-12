from email.policy import default
from django.db import models
from django.contrib.auth.models import User 
from blog.models.category import Category
import readtime
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish = models.BooleanField(default=False)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/posts', default='', null=True, blank=True)
    file = models.FileField(upload_to='images/files', default='', null=True, blank=True)
    description = RichTextUploadingField(default='')
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-added_on']

    def __str__(self):
        return self.title

    def get_readtime(self):
        return readtime.of_text(self.description)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=1)
    fullname = models.CharField(max_length=255)
    comment = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.fullname
    
    class Meta:
        ordering =['-added_on']