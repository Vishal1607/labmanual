from email import message
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# from models import AuthUser
# Create your views here.





def login(request):
    if request.method == 'POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            # thisUser = AuthUser.objects.get(authuser=request.user)
            return redirect('welcome.html') 
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('/')
    else:        
     return render(request,'R&L.html')
    
def registration(request):
    if request.method == 'POST':
         username=request.POST['username']
         password1=request.POST['password']
         email=request.POST['email']
         return redirect('/')
        #  if password1==password2:
        #      if User.objects.filter(username=username).exists():
        #          messages.info(request,'Username Taken')
        #          return redirect('registration')
        #         #  return render(request,'registration.html',{'error':'username already exists'})
        #      elif User.objects.filter(email=email).exists():
        #          messages.info(request,'Email Taken')
        #          return redirect('registration')
        #         #  return render(request,'registration.html',{'error':'email already exists'})
        #      user=User.objects.create_user(username=username,password=password1,email=email,first_name=firstname,last_name=lastname)
        #      user.save()
        #      print('user created')
        #      return render(request,'')

        #  else:
        #     messages.info(request,'Password not matching')
        #     return redirect('registration')
    else:
        return render(request,'R&L.html')        

   
       
    #   form=NewUserForm(request.POST)
    # if form.is_valid():
    #         user=form.save()
    #         login(request,user )
    #         message.success(request,f"New Account Created: {user.username}")
    #         return redirect("main:home")
    #         message.error(request,"Account Creation Failed")
    # form=NewUserForm()
    # return render(request=request,template_name="registration.html",context={"form":form})      
    # return render(request,'registration.html')