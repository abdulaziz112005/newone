from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, reverse
from .models import *
from news.models import Category
from django.http import HttpResponseRedirect


def contact(request):
    contacts = Contact.objects.get(pk=1)
    categorys = Category.objects.all()

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'contacts': contacts, 'form': form, 'categorys':categorys }
    return render(request, 'main/name.html' , context)


def next(request):
    return render(request, 'main/index.html', {})

