from django.shortcuts import render
from .models import Category, Tags, Articles



def index(request):
    fresh = Articles.objects.order_by('-create_at')[:5]
    news = Articles.objects.all()
    categorys = Category.objects.all()
    context = {
        'categorys': categorys,
        'news': news,
        'fresh':fresh 
    }
    return render(request, 'main/index.html', context)

def category(request):
    categories = Category.objects.all()
    tags = Tags.objects.all()
    articles = Articles.objects.all()
    categorys = Category.objects.all()
    context = {
        'categories': categories,
        'tags': tags,
        'articles': articles,
        'categorys': categorys
    }
    print(context)
    return render(request, 'main/category.html', context)

def view(request, id):
    try:
        view = Articles.objects.get(pk=id)
    except Articles.DoesNotExist:
        view = None
    context= {"view": view}
    return render(request, 'main/view.html', context)