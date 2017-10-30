from __future__ import unicode_literals
from django.shortcuts import render
from .tasks import download_data


def catch_data(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        url = request.POST.get('url')
        blog_url = request.POST.get('blog_url')

        download_data(title, url, blog_url)

    return render(request, 'template.html', {})


