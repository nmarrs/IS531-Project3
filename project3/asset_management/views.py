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

def search(request):
    if request.method == 'POST':
        asset_name =  request.POST.get('search')
        try:
            status = amod.Asset.objects.filter(name__icontains=asset_name)
        except amod.Asset.DoesNotExist:
            status = None
        return render(request,"index.html",{"assets":status})
    else:
        return render(request,"index.html",{})
