from django.shortcuts import render, redirect
# import user creation form
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def register_view(request):
    # Step 2: check if user is already authenticated
    if request.user.is_authenticated:
        return redirect('index') # redirect to home page
    
    # handle user registration
    # Step 1: handle user registration
    if request.method == 'POST': # form submission
        account_form = UserCreationForm(request.POST) # bind data to form
        if account_form.is_valid(): # validate form data
            account_form.save() # save user to database
            # return redirect('register')
            return redirect('login') # redirect to login page
    else:
        account_form = UserCreationForm()
    
    context = {
        'form': account_form,
    }
    return render(request, 'accounts/register_form.html', context)


def login_view(request):
    # Step 2: check if user is already authenticated
    if request.user.is_authenticated:
        return redirect('index') # redirect to home page
    
    # handle user login -> # Step 1: process the login form
    if request.method == 'POST': # form submission
        login_form = AuthenticationForm(request, data=request.POST) # bind data to form
        if login_form.is_valid(): # validate form data
            user = login_form.get_user() # get user object
            login(request, user) # log the user in
            return redirect('index') # redirect to home page
    else:
        login_form = AuthenticationForm()
        
    context = {
        'form': login_form,
    }
    return render(request, 'accounts/login_form.html', context)


def logout_view(request):
    # handle user logout
    logout(request)
    return redirect('login')
