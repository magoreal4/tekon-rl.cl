from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='Home'),
    path('download/pdf/<str:title>/', views.download_pdf, name='download_pdf')
]

