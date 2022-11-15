from blog.models.downloads import Download
from django.views import View
from django.shortcuts import render

class AllDownloads(View):
    def get(self, *args, **kwargs):
        all_downloads = Download.objects.all()
        context = {
            'all_downloads': all_downloads
        }
        return render(self.request, 'all_downloads.html', context)

def all_downloads(request):
    downloads = Download.objects.all()
    context = {
        'downloads': downloads
    }
    return context
