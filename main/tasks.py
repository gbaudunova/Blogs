from __future__ import unicode_literals
from celery import shared_task

@shared_task()
def download_data(title, url, blog_url):
    # def my_hook(d):
    #     if d['status'] == 'finished':
    #         print('Done downloading, now converting ...')
    print(title)
    print(url)
    print(blog_url)



