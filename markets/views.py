from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.views.decorators.http import require_http_methods

from itertools import chain

# CRUD DEVELOPERS

#------ Create ------
@require_http_methods(["POST"])
def createMarket(request):
    name = request.POST['nameInput']
    address = request.POST['addressInput']
    user_pk = request.POST['userInput']
    sponsored = request.POST.get('sponsoredInput', False)
    local_delivery = request.POST.get('localDeliveryInput', False)
    delivery_time = request.POST['deliveryTimeInput']
    delivery_cost = request.POST['deliveryCostInput']
    stars = request.POST['starsInput']

    user = User.objects.get(id=user_pk)

    Market.objects.using(user.shard).create(
        name=name,
        address=address,
        sponsored=sponsored,
        local_delivery=local_delivery,
        delivery_time=delivery_time,
        delivery_cost=delivery_cost,
        stars=stars,
        user_pk=user_pk,
    )
    messages.success(request, 'Mercado: ' + name +' ¡creado!')
    return redirect('/markets')

#------ List ------
@require_http_methods(["GET"])
def listMarket(request):
    market_1 = Market.objects.using('shard_1').all()
    market_2 = Market.objects.using('shard_2').all()
    market_3 = Market.objects.using('shard_3').all()

    objects = list(chain(market_1, market_2, market_3))
    return render(request, "markets/index.html", {
        "zone_1": market_1,
        "zone_2": market_2,
        "zone_3": market_3,
        "objects": objects,
    })


#------ Edit ------
@require_http_methods(["GET","POST"])
def editMarket(request, zone, slug):
    ZONE_MAP = {
        1: 'shard_1',
        2: 'shard_2',
        3: 'shard_3',
    }
    market = Market.objects.using(ZONE_MAP[zone]).get(slug=slug)

    if request.method == 'POST':
        name = request.POST['nameInput']
        address = request.POST['addressInput']

        market.name = name
        market.address = address
        market.save()
        messages.success(request, 'Mercado: ' + name +' ¡editado!')
        return redirect('/markets')

    return render(request, "markets/edit.html", {"market": market, "zone": zone})

#------ Delete ------
@require_http_methods(["GET"])
def deleteMarket(request, zone, slug):
    ZONE_MAP = {
        1: 'shard_1',
        2: 'shard_2',
        3: 'shard_3',
    }
    market = Market.objects.using(ZONE_MAP[zone]).get(slug=slug)

    market.delete()
    messages.success(request, 'Mercado eliminado!')
    return redirect('/markets')  
