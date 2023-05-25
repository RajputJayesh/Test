from django.urls import path
from vehicle_management_app import views
urlpatterns = [
    path('info',views.vehicle_info),
    path('',views.index),
    path('read',views.readdata),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
]