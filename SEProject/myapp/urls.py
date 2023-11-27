from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'myapp'
urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name="home"),
    path('signup', views.signup, name="signup"),
    path("menu/", views.menu, name="menu"),
    path("profile", views.profile, name="profile"),
    path("cart", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name= "add"),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="add")
]
