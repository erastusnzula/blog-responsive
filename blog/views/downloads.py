from blog.models.downloads import Download


def all_downloads(request):
    downloads = Download.objects.all()
    context = {
        'downloads': downloads
    }
    return context