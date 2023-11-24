from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'myapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='authtest.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('apereo', views.ApereoView.as_view(), name='apereo'),
    path('manual', views.ManualProtect.as_view(), name='manual'),
    path('protect', views.ProtectView.as_view(), name='protect'),
    path('python', views.DumpPython.as_view(), name='python'),

    path('signup', views.signup, name="SignUp"),
    path("menu/", views.menu, name="Menu"),
    path('json', views.entree_Json, name="Json")
    
]
