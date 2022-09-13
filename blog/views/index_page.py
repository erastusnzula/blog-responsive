from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View
from blog.models.post import Post, Comment
from blog.models.contact import Contact
from blog.models.category import Category
from blog.models.subscription import NewsLetter


class IndexPage(View):
    def get(self, *args, **kwargs):
        posts = Post.objects.all().filter(publish=True)
        categories = Category.objects.all()
        context = {
            'posts': posts,
            'categories': categories,
        }
        return render(self.request, 'index_page.html', context)

    def post(self, *args, **kwargs):
        email_address = self.request.POST.get("email")
        subscribe_email = self.request.POST.get('subscribe-email')
        message = self.request.POST.get('message')
        search_title = self.request.POST.get('search-title')
        if (email_address is not None) and (message is not None):
            Contact(
                email_address=email_address,
                message=message
            ).save()
            messages.success(self.request, 'Sent successfully.')
            return redirect("blog:index-page")

        elif subscribe_email:
            NewsLetter(
                email=subscribe_email
            ).save()
            messages.success(self.request, 'Subscribed successfully.')
            return redirect("blog:index-page")
        else:
            if search_title is not None:
                posts = Post.objects.filter(title__contains=search_title, publish=True)
                if posts:
                    categories = Category.objects.all()
                    context = {
                        'posts': posts,
                        'categories': categories
                    }
                    return render(self.request, 'category.html', context)
                else:
                    messages.warning(self.request, "Oops!! No article under that title.")
                    return redirect("blog:index-page")


class PostDetails(View):
    def get(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        categories = Category.objects.all()
        posts = Post.objects.all().filter(publish=True)
        comments = Comment.objects.filter(post=post)

        context = {
            'post': post,
            'posts': posts,
            'categories': categories,
            'comments': comments
        }

        return render(self.request, 'post_details.html', context)

    def post(self, request, id, *args, **kwargs):
        post = Post.objects.get(id=id)
        fullname = self.request.POST.get("fullname")
        comment = self.request.POST.get('comment-message')
        email_address = self.request.POST.get("email")
        subscribe_email = self.request.POST.get('subscribe-email')
        message = self.request.POST.get('message')
        search_title = self.request.POST.get('search-title')
        if (email_address is not None) and (message is not None):
            Contact(
                email_address=email_address,
                message=message
            ).save()
            messages.success(self.request, 'Sent successfully')
            return redirect("blog:post-details", id=id)
        elif (fullname is not None) and (comment is not None):
            Comment(
                post=post,
                fullname=fullname,
                comment=comment
            ).save()
            messages.success(self.request, 'Sent successfully')
            return redirect("blog:post-details", id=id)
        elif subscribe_email:
            NewsLetter(
                email=subscribe_email
            ).save()
            messages.success(self.request, 'Subscribed successfully.')
            return redirect("blog:post-details", id=id)
        else:
            if search_title is not None:
                posts = Post.objects.filter(title__contains=search_title, publish=True)
                if posts:
                    categories = Category.objects.all()
                    context = {
                        'posts': posts,
                        'categories': categories
                    }
                    return render(self.request, 'category.html', context)
                else:
                    messages.warning(self.request, "Oops!! No article under that title.")
                    return redirect("blog:post-details", id=id)
