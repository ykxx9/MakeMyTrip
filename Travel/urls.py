
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

    path('hotels/', views.hotels, name='hotels'),
    path('hotels/results/', views.hotel_results, name='hotel_results'),

    path('homestays/', views.coming_soon,
         {'service_key': 'homestays'}, name='homestays'),

    path('holidays/', views.service_page,
         {'page_title': 'Holiday Packages'}, name='holidays'),

    path('trains/', views.coming_soon,
         {'service_key': 'trains'}, name='trains'),

    path('buses/', views.coming_soon,
         {'service_key': 'buses'}, name='buses'),

    path('cabs/', views.coming_soon,
         {'service_key': 'cabs'}, name='cabs'),

    path('tours/', views.coming_soon,
         {'service_key': 'tours'}, name='tours'),

    path('visa/', views.coming_soon,
         {'service_key': 'visa'}, name='visa'),

    path('forex/', views.coming_soon,
         {'service_key': 'forex'}, name='forex'),

    path('insurance/', views.coming_soon,
         {'service_key': 'insurance'}, name='insurance'),

    path('flights/results/', views.flight_results,
         name='flight_results'),
]
