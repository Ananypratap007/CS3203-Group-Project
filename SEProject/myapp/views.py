from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.http import HttpResponse
from django.core import serializers
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode
from .forms import SignupForm
from .models import EntreeItem, AppetizerItem, BeverageItem, DesertItem, SideItem


def home(request):
    return render(request, "menu.html")

def menu(request):
    eitems = EntreeItem.objects.all()
    aitems = AppetizerItem.objects.all()
    sitems = SideItem.objects.all()
    bitems = BeverageItem.objects.all()
    ditems = DesertItem.objects.all()
    index = {
        "entree": eitems,
        "app" : aitems,
        "side" : sitems,
        "bev" : bitems,
        "desert" : ditems

    }
    return render(request, "menu.html", index)

def entree_Json(request):
    data = serializers.serialize('json  ', EntreeItem.objects.all())
    return HttpResponse(data, content_type='application/json')


class OpenView(View) :
    def get(self, request):
        return render(request, 'home.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'home.html')

class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'home.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'home.html')

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/">Go back</a>"""
        return HttpResponse(resp)

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})