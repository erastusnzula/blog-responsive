from django.shortcuts import render,redirect
from django.contrib import messages
from django.views import View
from blog.models.post import Post,Comment
from blog.models.contact import Contact
from blog.models.category import Category
from blog.models.subscription import NewsLetter


class PostsByCategory(View):
    def get(self, request, category, *args, **kwargs):
        posts = Post.objects.filter(category__name__contains=category, publish=True)
        if posts:
            categories = Category.objects.all()
            context = {
                'posts': posts,
                'categories': categories
            }

            return render(self.request, 'category.html', context)
        else:
            messages.warning(self.request, "Ooops!! Article yet to be publically published.")
            return redirect("blog:index-page")
        
    def post(self, request, category,*args, **kwargs):
        email_address = self.request.POST.get("email")
        subscribe_email = self.request.POST.get('subscribe-email')
        message = self.request.POST.get('message')
        search_title= self.request.POST.get('search-title')
        if (email_address != None) and(message != None):
            Contact(
                email_address=email_address,
                message=message
            ).save()
            messages.success(self.request, 'Sent successfuly.')
            return redirect("blog:category",category=category)
        elif subscribe_email:
            NewsLetter(
                email = subscribe_email
            ).save()
            messages.success(self.request, 'Subscribed successfuly.')
            return redirect("blog:category",category=category)
        
        else:
            if search_title != None:
                posts = Post.objects.filter(title__contains=search_title, publish=True)
                if posts:
                    categories = Category.objects.all()
                    context = {
                        'posts': posts,
                        'categories': categories
                        }
                    return render(self.request, 'category.html', context)
                else:
                    messages.warning(self.request, "Ooops!! No article under that title.")
                    return redirect("blog:category",category=category)

