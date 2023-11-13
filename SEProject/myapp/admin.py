from django.contrib import admin
from .models import EntreeItem, AppetizerItem, BeverageItem, DesertItem, SideItem

# Register your models here.
admin.site.register(EntreeItem)
admin.site.register(AppetizerItem)
admin.site.register(BeverageItem)
admin.site.register(DesertItem)
admin.site.register(SideItem)