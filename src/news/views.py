from django.shortcuts import render
from .models import Category, Tags, Articles


def index(request):
    return render(request, 'main/index.html')

def category(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    articles = Articles.objects.all()
    context = {
        'categories': categories,
        'tags': tags,
        'articles': articles
    }
    print(context)
    return render(request, 'main/category.html', context)