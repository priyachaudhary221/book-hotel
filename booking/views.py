from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import RegisterForm, BookingForm
from .models import Service, Booking


def home(request):
    services = Service.objects.filter(available=True)

    return render(
        request,
        'booking/home.html',
        {'services': services}
    )


def register_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            messages.success(
                request,
                'Registration successful. Please login.'
            )

            return redirect('login')

    else:
        form = RegisterForm()

    return render(
        request,
        'booking/register.html',
        {'form': form}
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        messages.error(
            request,
            'Invalid username or password.'
        )

    return render(
        request,
        'booking/login.html'
    )


def logout_view(request):

    logout(request)

    return redirect('home')


@login_required
def create_booking(request):

    if request.method == 'POST':

        form = BookingForm(request.POST)

        if form.is_valid():

            booking = form.save(commit=False)

            booking.user = request.user

            booking.status = 'Pending'

            booking.save()

            messages.success(
                request,
                'Your booking has been created successfully.'
            )

            return redirect('my_bookings')

    else:

        form = BookingForm()

    return render(
        request,
        'booking/book.html',
        {'form': form}
    )


@login_required
def my_bookings(request):

    bookings = Booking.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'booking/my_bookings.html',
        {'bookings': bookings}
    )


@login_required
def cancel_booking(request, booking_id):

    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user
    )

    if booking.status == 'Pending':

        booking.status = 'Cancelled'

        booking.save()

        messages.success(
            request,
            'Booking cancelled successfully.'
        )

    return redirect('my_bookings')