"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from markets.admin import admin_shard1, admin_shard2, admin_shard3

urlpatterns = [
    path('', include('markets.urls')),
    path('admin/', admin.site.urls, name='admin'),
    # ADMIN
    path('admin-shard1/', admin_shard1.urls, name='admin_shard_1'),
    path('admin-shard2/', admin_shard2.urls, name='admin_shard_2'),
    path('admin-shard3/', admin_shard3.urls, name='admin_shard_3'),
]
