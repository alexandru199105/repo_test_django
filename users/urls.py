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
from users.views import *

urlpatterns = [
    path('', UsersListView.as_view(), name='users-all'),
    path('add/', CreateUserView.as_view(), name='users-add'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='users-detail'),
    path('edit/<int:pk>', UsersUpdateView.as_view(), name='users-edit'),
    path('delete/<int:pk>', UsersDeleteView.as_view(), name='users-delete'),
]
