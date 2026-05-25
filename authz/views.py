from django.shortcuts import render,redirect,resolve_url
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
class Signup(View):
    def get(self,request):
        return render(request,'signup.html')
    def post(self,request):
        username=request.POST.get('username')
        email=request.POST.get('email')
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        password=request.POST.get('password')
        if not username or not email or not firstname or not lastname or not password:
            messages.error(request,'all field are required')
            return render(request,'signup.html')
        if len(password)<8:
            messages.error(request,'password too short')
            return render(request,'signup.html')
        if len(username)<5:
            messages.error(request,'username too short')
            return render(request,'signup.html')
        

        username = username.lower()
        email = email.lower()
        if User.objects.filter(username=username).exists():
            messages.error(request,'username already exist')
            return render(request,'signup.html')
        if User.objects.filter(email=email).exists():
            messages.error(request,'email already taken')
            return render(request,'signup.html')

        

        user= User.objects.create(username=username, email=email, first_name=firstname,last_name=lastname)
        user.set_password(password)
        user.save()
        messages.success(request,'account created successfully')

        return redirect(resolve_url('home'))
    
class loginView(View):
    def get(self,request):
         return render (request,'login.html')
    def post(self,request): 
        next_page=request.GET.get('next') 
        username=request.POST.get('username')
        password=request.POST.get('password')
        if not username or not password:
            messages.error(request,'all fields required')
            return render(request,'login.html')
        username=username.lower()
        username_exist=User.objects.filter(username=username).first()
        if not username_exist:
            messages.error(request,'invalid login credentials')
            return render(request,'login.html')
        user= authenticate(username=username, password=password)
        if not user:
            messages.error(request,'invalid login credentials')
            return render(request,'login.html')
        login(request,user)
        messages.success(request,'login successful')
        return redirect(next_page or resolve_url('home'))

def logoutView(request):
    logout(request)
    return redirect(resolve_url('login'))
            
            
            

    
# Create your views here.
