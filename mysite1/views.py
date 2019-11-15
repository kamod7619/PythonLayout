'''
 Developed by Mr Kamod Kumar(Software Engineer)
'''
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):

        return render(request,'index.html')

'''
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
'''

def blog(request):
        return render(request, 'blog.html')


def about(request):
    return render(request,'about.html')
