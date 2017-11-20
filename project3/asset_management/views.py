from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from asset_management import models as amod


def index(request):
    asset_list = amod.Asset.objects.order_by('-date_implemented')
    params = {
        'asset_list': asset_list,
    }
    return render(request, 'index.html', params)
