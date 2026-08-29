from django import forms
from .models import Booking
from django.contrib.auth.models import User


class RegisterForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Enter a secure password',
            'autocomplete': 'new-password',
        })
    )

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
        ]

        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder': 'Choose a username',
                'autocomplete': 'username',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'you@example.com',
                'autocomplete': 'email',
            }),
        }


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking

        fields = [
            'service',
            'booking_date',
            'booking_time',
            'check_in',
            'check_out',
        ]

        widgets = {

            'service': forms.Select(attrs={
                'class': 'form-control',
            }),

            'booking_date': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'booking_time': forms.TimeInput(
                attrs={
                    'type': 'time'
                }
            ),

            'check_in': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),

            'check_out': forms.DateInput(
                attrs={
                    'type': 'date'
                }
            ),
        }

        labels = {
            'service': 'Select Room',
            'booking_date': 'Booking Date',
            'booking_time': 'Booking Time',
            'check_in': 'Check-in Date',
            'check_out': 'Check-out Date',
        }
