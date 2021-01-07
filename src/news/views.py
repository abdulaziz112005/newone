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
    articles = Articles.objects.select_related('category').all()
    categorys = Category.objects.all()
    context = {
        'articles': articles,
        'categorys': categorys
    }
    print(context)
    return render(request, 'main/category.html', context)

def view(request, slug):
    news = Articles.objects.order_by('-create_at')[:5]
    try:
        article = Articles.objects.get(slug=slug)
        article.views_count =article.views_count + 1
        article.save()
        tags = article.tags.all()
    except Articles.DoesNotExist:
        article = None
    context= {'article': article,
              'categorys': categorys,
              'news': news,
              'tags': tags
              }
    return render(request, 'main/view.html', context)