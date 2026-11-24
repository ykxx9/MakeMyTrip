
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('offers/', views.offers, name='offers'),

    path('my-trips/', views.service_page,
         {'page_title': 'My Trips'}, name='my_trips'),

    path('login/', views.service_page,
         {'page_title': 'Login'}, name='login'),

    path('signup/', views.service_page,
         {'page_title': 'Sign Up'}, name='signup'),

    path('flights/', views.flight_search, name='flights'),

    path('hotels/', views.service_page,
         {'page_title': 'Hotels'}, name='hotels'),

    path('homestays/', views.service_page,
         {'page_title': 'Villas & Homestays'}, name='homestays'),

    path('holidays/', views.service_page,
         {'page_title': 'Holiday Packages'}, name='holidays'),

    path('trains/', views.service_page,
         {'page_title': 'Trains'}, name='trains'),

    path('buses/', views.service_page,
         {'page_title': 'Buses'}, name='buses'),

    path('cabs/', views.service_page,
         {'page_title': 'Cabs'}, name='cabs'),

    path('tours/', views.service_page,
         {'page_title': 'Tours & Attractions'}, name='tours'),

    path('visa/', views.service_page,
         {'page_title': 'Visa'}, name='visa'),

    path('forex/', views.service_page,
         {'page_title': 'Forex'}, name='forex'),

    path('insurance/', views.service_page,
         {'page_title': 'Travel Insurance'}, name='insurance'),

    path('flights/results/', views.flight_results,
         name='flight_results'),
]
