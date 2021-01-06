from .forms import NameForm
from django.shortcuts import render, get_object_or_404, reverse
from .models import *
from django.http import HttpResponseRedirect


def contact(request):
    contacts = Contact.objects.get(pk=1)


    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('news:form'))
    else:
        form = NameForm()

    context = {'contacts': contacts, 'form': form }
    return render(request, 'main/name.html' , context)


def next(request):
    return render(request, 'main/index.html', {})

