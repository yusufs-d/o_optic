"""optic URL Configuration

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
from django.urls import path
from index.views import *
from user.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage/', index, name= "index"),
    path('customer/',customer,name="customer"),
    path('add-customer/',add_customer,name="add_customer"),
    path('delete-customer/<int:id>/',delete_customer, name="delete_customer"),
    path('edit-customer/<int:id>/',edit_customer,name="edit_customer"),
    path('debts/', debts,name="debts"),
    path('income/', income,name="income"),
    path('add-expense/',add_expense,name="add_expense"),
    path('delete-expense/<int:id>/',delete_expense, name="delete_expense"),
    path('',loginUser,name="loginUser"),
    path('logout/',logoutUser,name="logoutUser")




]
