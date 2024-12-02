from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', list, name="listc"),
    path('up/<str:pk>/', update.as_view(), name='update'),
]