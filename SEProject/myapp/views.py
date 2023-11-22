from django.shortcuts import render, HttpResponse
from django.core import serializers
from .models import EntreeItem, AppetizerItem, BeverageItem, DesertItem, SideItem

def home(request):
    return render(request, "home.html")

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