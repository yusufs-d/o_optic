from operator import imod
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import login,authenticate,logout
from index.views import *


def loginUser(request):
    username = request.POST.get('username')
    password = str(request.POST.get('password'))
    if request.method == "POST":
        aut = authenticate(username = username,password = password)
        if aut == None:
            messages.error(request,"E-posta ya da parola hatalı")
            return redirect("loginUser")
        else:
            login(request,aut)
            return redirect("index")

    return render(request,"login.html")



def logoutUser(request):
    user = request.user
    logout(request)
    return redirect("loginUser")