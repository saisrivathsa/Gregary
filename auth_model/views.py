from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
#for authentication uses
from django.contrib import auth
# for  user
from django.contrib.auth.models import User

def logout(request) :
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth_model:login'))

#gets values from the form and checks whether user exists
def authenticate_method(request) :
    username = request.POST.get('username', '' )
    password = request.POST.get('password', '' )
    user = auth.authenticate( username=username, password=password )
    # The default value when a user is not found is none
    if user is not None :
        auth.login( request, user)
        return HttpResponseRedirect(reverse("gregary:index"))
    else :
        return render(request, "auth_model/login.html", {'error':'Invalid Credentials'})
        # Takes back to login page with an error message

# Creates a new user by taking name, mail, mobile number and password
def create_new_user(request) :
    try:
        user = User.objects.create_user(
        username = request.POST['username'],
        password = request.POST['password'],
        email = request.POST['email'],
        )
        # Default fields for user class in django doesn't contain certain fields which can be added using extra_fields
        user.extra_fields = {'phone_number' : request.POST['phone_number']}
        # Saving the user data
        user.save()
        username = request.POST.get('username', '' )
        password = request.POST.get('password', '' )
        # Logging in the user after creating the new user
        user = auth.authenticate( username=username, password=password )
        return HttpResponse('<h2>Created new user %s </h2><br><a href="../sign_up/">  create another account?</a>' %user.username)
    except :
        return render( request, 'auth_model/sign_up.html', {'error':'Error making account. Try again'} )
        # Returning to signup page in case of error in making the account
