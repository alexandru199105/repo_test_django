"""
URL configuration for small_business project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from servicii.views import ServiciiDetailsView, ServiciiListView, ServiciiUpdateView, ServiciiDeleteView, \
    ServiciiCreateView
from home.views import HomeView

urlpatterns = [
    path('', ServiciiListView.as_view(), name='serviciu-all'),
    path('detail/<int:pk>', ServiciiDetailsView.as_view(), name='serviciu-detail'),
    path('update/<int:pk>', ServiciiUpdateView.as_view(), name='serviciu-edit'),
    path('delete/<int:pk>', ServiciiDeleteView.as_view(), name='serviciu-delete'),
    path('add/', ServiciiCreateView.as_view(), name='add-serviciu'),
]
