from django.contrib import admin
from .models import Service, Booking


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available',)
    search_fields = ('name',)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'service',
        'booking_date',
        'booking_time',
        'status',
    )

    list_filter = (
        'status',
        'booking_date',
        'service',
    )

    search_fields = (
        'user__username',
        'service__name',
    )

    list_editable = ('status',)