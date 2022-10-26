from django.shortcuts import HttpResponse, render

# Create your views here.
def index(requests):
    return HttpResponse('Главная страница')

def group_posts(requests):
    return HttpResponse('Страныца постов')

