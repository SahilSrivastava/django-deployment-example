from django.shortcuts import render
from my_app.forms import UserProfileInfoForm,UserForm

from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'my_app/index.html')


def register(request):
    registered=False

    if request.method=="POST":
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)#  HASHING THE PASSWORD
            user.save() #SAVING AGAIN TO SAVE THE HASHED PASSWORD

            profile=profile_form.save(commit=False)
            profile.user=user # TO SET ONE TO ONE RELATIONSHIP

            if 'profile_pic' in request.FILES:
                profile.profile_pic=request.FILES['profile_pics']
            profile.save()
            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()
    return render(request,'my_app/registration.html',
                {'user_form':user_form,
                'profile_form':profile_form,
                'registered':registered}
    )


def user_login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed!")
            return render(request,'my_app/login.html')
    else:
        return render(request,'my_app/login.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def special(request):
    return HttpResponse("You are logged in!")
