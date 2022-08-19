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

    Car.objects.using(zone).create(name=name, company=company)
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
def editCar(request, slug):
    car = Car.objects.get(slug=slug)

    if request.method == 'POST':
        name = request.POST['nameInput']
        company = request.POST['companyInput']

        car.name = name
        car.company = company
        car.save()
        messages.success(request, 'Vehículo: ' + name +' ¡editado!')
        return redirect('/cars')

    return render(request, "cars/edit.html", {"car": car})

#------ Delete ------
@require_http_methods(["GET"])
def deleteCar(request, slug):
    car = Car.objects.get(slug=slug)

    car.delete()
    messages.success(request, '¡Vehículo eliminado!')
    return redirect('/cars')  