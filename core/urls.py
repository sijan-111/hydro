from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('projects/', views.projects, name='projects'),
    path('reports/', views.reports, name='reports'),
    path('downloads/', views.downloads, name='downloads'),
    path('notice/', views.notice, name='notice'),
    path('contact/', views.contact, name='contact'),
    path('clients/', views.clients, name='clients'),
    path('subscribe/', views.subscribe_newsletter, name='subscribe_newsletter'),
]
