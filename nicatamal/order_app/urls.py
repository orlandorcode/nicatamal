from django.urls import path
from order_app import views

# TEMPLATE TAGGING

app_name = 'order_app'

urlpatterns = [
    path('',  views.index, name = 'index'),
    path('order_form/', views.NewOrder, name='NewOrder'),
    path('client_form/', views.NewClient, name='NewClient'),
    path('register/', views.register, name = 'register'),
    path('user_login/', views.user_login, name='user_login'),
    ]