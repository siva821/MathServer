from django.contrib import admin 
from django.urls import path

urlpatterns = [ path('admin/', admin.site.urls), ]

from mathapp import views

urlpatterns = [ path('admin/', admin.site.urls), path('',views.power,name='home'),]
