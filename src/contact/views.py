from .forms import NameForm
from django.shortcuts import render, get_object_or_404, reverse
from .models import *
from news.models import Category
from django.http import HttpResponseRedirect


def contact(request):
    contacts = Contact.objects.get(pk=1)
    categorys = Category.objects.all()

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('news:form'))
    else:
        form = NameForm()

    context = {'contacts': contacts, 'form': form, 'categorys':categorys }
    return render(request, 'main/name.html' , context)


def next(request):
    return render(request, 'main/index.html', {})

