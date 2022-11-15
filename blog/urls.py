from django.urls import path
from blog.views.index_page import IndexPage, PostDetails
from blog.views.category import PostsByCategory
from blog.views.downloads import AllDownloads

app_name = 'blog'
urlpatterns = [
    path('', IndexPage.as_view(), name='index-page'),
    path('category/<category>/', PostsByCategory.as_view(), name='category'),
    path('post/<int:id>/', PostDetails.as_view(), name='post-details'),
    path('apps/download/', AllDownloads.as_view(), name='downloads'),
]
