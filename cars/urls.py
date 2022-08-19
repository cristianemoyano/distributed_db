from django.urls import path
from . import views

urlpatterns = [

    # Urls Developers
    path('', views.listCar, name='index'),
    path('register/', views.createCar),
    path('edit/<slug:slug>', views.editCar, name='editUrl'),
    path('delete/<slug:slug>', views.deleteCar, name='deleteUrl'),

]