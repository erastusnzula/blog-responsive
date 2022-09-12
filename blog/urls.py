from django.urls import path
from blog.views.index_page import IndexPage, PostDetails
from blog.views.category import PostsByCategory

app_name = 'blog'
urlpatterns = [
    path('', IndexPage.as_view(), name='index-page'),
    path('category/<category>/', PostsByCategory.as_view(), name='category'),
    path('post/<int:id>/', PostDetails.as_view(), name='post-details'),
]
