from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('register/', views.register_view, name='register'),

    path('login/', views.login_view, name='login'),

    path('logout/', views.logout_view, name='logout'),

    path('book/', views.create_booking, name='create_booking'),

    path('my-bookings/', views.my_bookings, name='my_bookings'),

    path(
        'cancel/<int:booking_id>/',
        views.cancel_booking,
        name='cancel_booking'
    ),
]