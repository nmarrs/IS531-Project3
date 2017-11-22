from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from asset_management import models as amod


def index(request):
    ''' View function that handles serving up the asset list to be displayed on index.html '''
    # if search param is passed process search query
    if request.GET.get('search'):
        asset_search_query = request.GET.get('search')
        try:
            # long query unions all of the results together as to search across all attributes of an asset
            asset_list = amod.Asset.objects.filter(Q(name__name__icontains=asset_search_query) | Q(location__office_location__icontains=asset_search_query) | Q(tag__icontains=asset_search_query) | Q(organization__name__icontains=asset_search_query) | Q(employee__name__icontains=asset_search_query) | Q(manufacturer__name__icontains=asset_search_query) | Q(manufacturer__part_number__icontains=asset_search_query) | Q(date_acquired__icontains=asset_search_query) | Q(description__icontains=asset_search_query) | Q(maintenance_notes__icontains=asset_search_query))
        except amod.Asset.DoesNotExist:
            # just a failsafe to handle any exceptions
            asset_list = None
    # else just serve up all assets
    else:
        asset_list = amod.Asset.objects.order_by('-date_acquired')

    params = {
        'asset_list': asset_list,
    }

    return render(request, 'index.html', params)
