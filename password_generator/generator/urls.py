from django.urls import path
from . import views

urlpatterns = [
    path('generate_password/', views.generate_password, name='generate_password'),
    path('save_password/', views.save_password, name='save_password'),
    path('saved_passwords/', views.saved_passwords, name='saved_passwords'),
    path('delete_password/<int:password_id>/', views.delete_password, name='delete_password'),
]
