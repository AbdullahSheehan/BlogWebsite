from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .forms import SignUpForm, ProfileChangeForm, ProfilePic
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

def registerUser(req):
    form = SignUpForm()
    registered = False
    if(req.method == 'POST'):
        form = SignUpForm(req.POST)
        if (form.is_valid()):
            form.save()
            registered=True
            return HttpResponseRedirect(reverse('Applogin:login'))
    return render(req, 'Applogin/register.html', context = {'form':form, 'registered':registered})
def loginUser(req):
    form = AuthenticationForm()
    hasError = False
    if(req.method == 'POST'):
        form = AuthenticationForm(data=req.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if(user is not None):
                login(req, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                hasError = True
        else:
            hasError = True
    return render(req, 'Applogin/login.html', context = {'form':form, 'error':hasError})
def logoutUser(req):
    logout(req)
    return HttpResponseRedirect(reverse('Applogin:login'))
def profileUser(req):
    return render(req, 'Applogin/profile.html', context = {})
def editProfile(req):
    current_user = req.user
    form = ProfileChangeForm(instance=current_user)
    if(req.method == 'POST'):
        form = ProfileChangeForm(req.POST, instance=current_user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Applogin:profile'))
    return render(req, 'Applogin/editProfile.html', context = {'form':form})
def addPicture(req):
    form = ProfilePic()
    if req.method == 'POST':
        form = ProfilePic(req.POST, req.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = req.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Applogin:profile'))
    return render(req, 'Applogin/addPic.html', context = {'form':form})
def changePicture(req):
    form = ProfilePic(instance=req.user.user_info)
    if req.method == 'POST':
        form = ProfilePic(req.POST, req.FILES, instance=req.user.user_info)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('Applogin:profile'))
    return render(req, 'Applogin/addPic.html', context = {'form':form})
def passwordChange(req):
    current_user = req.user
    form = PasswordChangeForm(current_user)
    if(req.method=="POST"):
        form = PasswordChangeForm(current_user, data=req.POST)
        if form.is_valid():
            form.save()
            login(req, current_user)
            return HttpResponseRedirect(reverse('Applogin:profile'))
    return render(req, 'Applogin/editPass.html', context = {'form':form})