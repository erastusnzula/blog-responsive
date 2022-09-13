from atexit import register
from django.contrib import admin
from blog.models.post import Post, Comment
from blog.models.category import Category
from blog.models.contact import Contact
from blog.models.subscription import NewsLetter
from blog.models.downloads import Download


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    pass


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    pass
