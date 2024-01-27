from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # redirect to main page
                return redirect('login')
            else:
                # Invalid login
                return render(request, 'users/login.html', {'form': form, 'error_message': 'Invalid Username or password'})
        else:
            form = LoginForm()
        return render(request, 'users/login.hmtl', {'form':form})

def signup_view(request):
    if request.method  == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('login')
        else:
            form = SignUpForm()
        return render(request, 'users/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
