from .forms import ProductForm
from django.shortcuts import render, get_object_or_404, reverse
from .models import *
from django.http import HttpResponseRedirect


def contact(request):
    contacts = Contact.objects.get(pk=1)

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'contacts': contacts, 'form': form }
    return render(request, 'main/name.html', context)


def next(request):
    return render(request, 'main/index.html', {})

