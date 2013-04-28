# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse

from puns.models import Pun
from puns.forms import PunCreateForm

def index(request):
    latest_pun_list = Pun.objects.order_by('-pub_date')[:20]

    context = {
        'latest_pun_list': latest_pun_list,
    }

    return render(request, 'puns/index.html', context)

def create(request):
    errors = []

    if request.method == 'POST':
        form = PunCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            pun = Pun(
                name = cd['name'],
                description = cd['description'],
                pub_date = timezone.now(),
                vote = 0
            )
            pun.save();

            return HttpResponseRedirect(reverse('puns:index', args=[]))
        else:
            form = PunCreateForm(request.POST)
    else:
        form = PunCreateForm()

    return render(request, 'puns/create.html', {'form': form})

def vote(request, pun_id):
    pun = get_object_or_404(Pun, pk=pun_id)
    pun.vote += 1;
    pun.save()

    return HttpResponseRedirect(reverse('puns:index', args=[]))

def delete(request, pun_id):
    pun = get_object_or_404(Pun, pk=pun_id)
    pun.delete();

    return HttpResponseRedirect(reverse('puns:index', args=[]))
