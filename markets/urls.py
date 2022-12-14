from django.urls import path
from . import views

urlpatterns = [

    # Markets
    path('', views.listMarket, name='list_markets'),
    path('add/', views.createMarket, name='add_markets'),
    path('edit/<str:zone>/<slug:slug>/', views.editMarket, name='edit_markets'),
    path('delete/<str:zone>/<slug:slug>/', views.deleteMarket, name='delete_markets'),
]