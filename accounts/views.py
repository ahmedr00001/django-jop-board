from django.shortcuts import render , redirect
from .form import SignupForm  , UserForm , ProfileForm
from django.contrib.auth import authenticate , login
from .models import Profile


def signup (request):
    
    if request.method =="POST":
        form = SignupForm(request.POST)
        if form.is_valid ():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username , password = password)
            login(request , user)
            return redirect ('accounts/profile')
    else :
        form = SignupForm()
    return render(request , 'registration/signup.html' , {"form":form})

def profile(request):
    profile = Profile.objects.get(user=request.user)

    return render(request , 'profile.html' , {'profile':profile})

def profile_edit(request):
    profile = Profile.objects.get(user=request.user)
    
    if request.method == "POST":
        userform = UserForm(request.POST,request.FILES, instance= request.user) 
        #we use instance = to tell django we want edit not create new object
        #also it display currnet info in form not empty form
        profileform = ProfileForm(request.POST,instance=profile)
        
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit= False)
            #we not save profile until give it it's user
            myprofile.user = request.user
            myprofile.save()
            
            return redirect('accounts:profile')  #we can use link name


    else:
        userform = UserForm(instance= request.user) 
        #we use instance = to tell django we want edit not create new object
        #also it display currnet info in form not empty form
        profileform = ProfileForm(instance=profile)

        context = {
            'userform' : userform,
            'profileform': profileform
        }  

    return render(request , 'profile_edit.html' , context)
