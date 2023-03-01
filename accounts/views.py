from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import authenticate , login
from .models import Profile
from django.shortcuts import get_object_or_404
from .forms import UserForm , ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from notes_App.models import Note
# Create your views here.
def home(request):
    pass



def register(request):
    if request.method == "POST":
        
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password= password)
            login(request, user)
            messages.info(request, 'register created successfully')
            return redirect('/notes')   
    else:
        form = UserCreationForm
    if request.user.is_authenticated:
        user = request.user
        profile = get_object_or_404(Profile , user=user)
        context = {
            'form': form,
            'profile':profile,
        }
    else:
        context = {
            'form': form,
        }
    return render(request,'signup.html', context)
    

def profile(request, slug):
        
        
        profile = get_object_or_404(Profile, slug=slug)
        context = {
            'profile': profile
        }
        
        return render(request,'profile.html',context)
    
def edit_profile(request,slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile) 
        if user_form.is_valid() and profile_form.is_valid() :
            user_form.save()
            profile_form.save()
            messages.info(request, 'Profile Updated successfully')
            # new_profile.user = request.user
            # new_profile.save()
            return redirect('/')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)  
        
        context = {
            'user_form':user_form,
            'profile_form':profile_form,
            'profile': profile,
            
        }  
        
        return render(request,'edit_profile.html',context)
    
    
def change_password(request,slug):
    profile = get_object_or_404(Profile, slug=slug)
    if request.method == 'POST':
        form =  PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            
            form.save()
            messages.info(request, 'Password Updated successfully')
            return redirect('/')
    else:
        form =  PasswordChangeForm(user=request.user)
    
    context = {
        'form': form,
        'profile':profile,
    }
    return render(request,'change_password.html',context)