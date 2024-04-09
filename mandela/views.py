from .models import Biography, Quote, Legacy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """
    Render the home page.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered home page.
    """
    return render(request, 'mandela/home.html')


def biography(request):
    """
    Render the biography page.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered biography page.
    """
    biography_content = Biography.objects.first()  # Assuming there's only one biography
    return render(request, 'mandela/biography.html', {'biography': biography_content})


def quotes(request):
    """
    Render the quotes page.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered quotes page.
    """
    quotes_list = Quote.objects.all()
    return render(request, 'mandela/quotes.html', {'quotes': quotes_list})


def legacy(request):
    """
    Render the legacy page.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered legacy page.
    """
    # Add logic to fetch legacy content if needed
    return render(request, 'mandela/legacy.html')


def user_login(request):
    """
    Render the user login page.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered user login page.
    """
    return render(request, 'authentication/user_login.html')


def authenticate_user(request):
    """
    Authenticate a user.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponseRedirect: Redirects to home page if authentication is successful, otherwise redirects to user login page.
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('home'))


def show_user(request):
    """
    Show user information.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered user information page.
    """
    print(request.user.username)
    return render(request, 'authentication/user.html', {
        "username": request.user.username,
        "password": request.user.password
    })


def register(request):
    """
    Render the registration page and handle user registration.

    Parameters:
    request (HttpRequest): The HTTP request.

    Returns:
    HttpResponse: Rendered registration page.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('user_login')  
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})
