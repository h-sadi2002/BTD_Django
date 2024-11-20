from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Citizen
from django.contrib.auth.hashers import make_password, check_password

def home(request):
    return render(request, 'citizen/index.html')

def citizen_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            citizen = Citizen.objects.get(username=username)
            if check_password(password, citizen.password):
                # Successful login
                request.session['citizen_id'] = citizen.id  # Store citizen ID in session
                return redirect('citizen:citizen_panel')  # Redirect to citizen panel after login
            else:
                messages.error(request, 'Invalid username or password')
        except Citizen.DoesNotExist:
            messages.error(request, 'Invalid username or password')
    return render(request, 'citizen/citizen_login.html')

def citizen_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if Citizen.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('citizen:citizen_register')

        if Citizen.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return redirect('citizen:citizen_register')

        # Hash the password before saving
        hashed_password = make_password(password)
        Citizen.objects.create(
            name=name,
            username=username,
            email=email,
            password=hashed_password
        )
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('citizen:citizen_login')

    return render(request, 'citizen/citizen_register.html')

def citizen_panel(request):
    # Check if the user is logged in
    if 'citizen_id' not in request.session:
        return redirect('citizen:citizen_login')  # Redirect to login if not logged in

    citizen_id = request.session['citizen_id']
    citizen = Citizen.objects.get(id=citizen_id)  # Get the logged-in citizen's details

    return render(request, 'citizen/citizen_panel.html', {'citizen': citizen})
def citizen_profile(request):
    # Check if the user is logged in
    if 'citizen_id' not in request.session:
        return redirect('citizen:citizen_login')  # Redirect to login if not logged in

    citizen_id = request.session['citizen_id']
    citizen = Citizen.objects.get(id=citizen_id)  # Get the logged-in citizen's details

    return render(request, 'citizen/citizen_panel.html', {'citizen': citizen})
def citizen_pass(request):
    # Check if the user is logged in
    if 'citizen_id' not in request.session:
        return redirect('citizen:citizen_login')  # Redirect to login if not logged in

    citizen_id = request.session['citizen_id']
    citizen = Citizen.objects.get(id=citizen_id)  # Get the logged-in citizen's details

    return render(request, 'citizen/citizen_panel.html', {'citizen': citizen})
def citizen_update(request):
    # Check if the user is logged in
    if 'citizen_id' not in request.session:
        return redirect('citizen:citizen_login')  # Redirect to login if not logged in

    citizen_id = request.session['citizen_id']
    citizen = Citizen.objects.get(id=citizen_id)  # Get the logged-in citizen's details

    return render(request, 'citizen/citizen_panel.html', {'citizen': citizen})

def logout(request):
    # Clear the session
    request.session.flush()  # This will remove all session data
    messages.success(request, 'You have been logged out successfully.')
    return redirect('citizen:citizen_login')  # Redirect to login page after logout