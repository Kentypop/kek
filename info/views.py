from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Company, servicehair

poststry = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 22222',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

girl= [
	{
	'name': 'mayaka',
	'love': 'lowaf',
	'descript': 'average'
	}
]


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'info/home.html', context)


def about(request):
    return render(request, 'info/about.html', {'title': 'About'})

def hometry(request):
    context = {
        'posts': poststry,
        'girls': girl,
        'companies': Company.objects.all(),
        'servicehairs': servicehair.objects.all()
    }
    return render(request, 'info/hometry.html', context)


def abouttry(request):
    return render(request, 'info/abouttry.html', {'title': 'About'})    