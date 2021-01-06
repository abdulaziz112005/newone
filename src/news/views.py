from django.shortcuts import render
from .models import Category


def index(request):
    return render(request, 'main/index.html')

def category(request):
    categories = Category.objects.all
    context = {
        'categories': categories
    }
    return render(request, 'main/category.html', context)