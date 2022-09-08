from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.views.decorators.http import require_http_methods

# CRUD DEVELOPERS

#------ Create ------
@require_http_methods(["POST"])
def createCar(request):
    name = request.POST['nameInput']
    company = request.POST['companyInput']
    zone = request.POST['zoneInput']
    user_pk = request.POST['userInput']

    Car.objects.using(zone).create(name=name, company=company, user_pk=user_pk)
    messages.success(request, 'Vehículo: ' + name +' ¡creado!')
    return redirect('/cars')

#------ List ------
@require_http_methods(["GET"])
def listCar(request):
    cars_1 = Car.objects.using('shard_1').all()
    cars_2 = Car.objects.using('shard_2').all()
    cars_3 = Car.objects.using('shard_3').all()

    return render(request, "cars/index.html", {"zone_1": cars_1,"zone_2": cars_2, "zone_3": cars_3})


#------ Edit ------
@require_http_methods(["GET","POST"])
def editCar(request, zone, slug):
    ZONE_MAP = {
        1: 'shard_1',
        2: 'shard_2',
        3: 'shard_3',
    }
    car = Car.objects.using(ZONE_MAP[zone]).get(slug=slug)

    if request.method == 'POST':
        name = request.POST['nameInput']
        company = request.POST['companyInput']

        car.name = name
        car.company = company
        car.save()
        messages.success(request, 'Vehículo: ' + name +' ¡editado!')
        return redirect('/cars')

    return render(request, "cars/edit.html", {"car": car, "zone": zone})

#------ Delete ------
@require_http_methods(["GET"])
def deleteCar(request, zone, slug):
    ZONE_MAP = {
        1: 'shard_1',
        2: 'shard_2',
        3: 'shard_3',
    }
    car = Car.objects.using(ZONE_MAP[zone]).get(slug=slug)

    car.delete()
    messages.success(request, '¡Vehículo eliminado!')
    return redirect('/cars')  


# CREATE ADDRESS

#------ Create ------
@require_http_methods(["POST"])
def createAddress(request):
    city:str = request.POST['cityInput']
    country:str = request.POST['countryInput']
    street_name:str = request.POST['street_nameInput']
    street_number:str = request.POST['street_number']
    user_pk:str = request.POST['userInput']

    address = Address.objects.create(
        city=city,
        country=country,
        street_name=street_name,
        street_number=street_number,
        user_id=user_pk,
    )
    messages.success(request, f'Dirección: {address} ¡creada!')
    return redirect('/cars/address')

#------ List ------
@require_http_methods(["GET"])
def listAddress(request):
    addresses = Address.objects.all()
    return render(request, "address/index.html", {"addresses": addresses})


#------ Edit ------
@require_http_methods(["GET","POST"])
def editAddress(request, id):
    address = Address.objects.get(id=id)

    if request.method == 'POST':
        city:str = request.POST['cityInput']
        country:str = request.POST['countryInput']
        street_name:str = request.POST['street_nameInput']
        street_number:str = request.POST['street_number']
        address.city = city
        address.country = country
        address.street_name = street_name
        address.street_number = street_number
        address.save()
        messages.success(request, f'Dirección: {address} editada!')
        return redirect('/cars/address')

    return render(request, "address/edit.html", {"address": address})

#------ Delete ------
@require_http_methods(["GET"])
def deleteAddress(request, id):
    address = Address.objects.get(id=id)
    address.delete()
    messages.success(request, '¡Dirección eliminada!')
    return redirect('/cars/address')  