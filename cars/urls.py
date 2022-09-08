from django.urls import path
from . import views

urlpatterns = [

    # Urls Developers
    path('', views.listCar, name='index'),
    path('register/', views.createCar),
    path('edit/<int:zone>/<slug:slug>/', views.editCar, name='editUrl'),
    path('delete/<int:zone>/<slug:slug>/', views.deleteCar, name='deleteUrl'),

    # Addresses
    path('address/', views.listAddress, name='indexAddress'),
    path('address/create/', views.createAddress, name='createAddress'),
    path('address/edit/<int:id>/', views.editAddress, name='editAddress'),
    path('address/delete/<int:id>/', views.deleteAddress, name='deleteAddress'),

]