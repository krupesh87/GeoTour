from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages 
from .models import Video
from .models import Info

# Create your views here.
def index(request):
    return render(request,'index.html')

def service(request):
    video=Video.objects.all()
    
    return render(request,'service.html',{"video":video}) 

def base(request):
    return render(request,'base.html')

def about(request):
    return render(request,'about.html')
 
def register(request):
    if request.method =='POST':
       username=request.POST['username']
       email=request.POST['email']
       password=request.POST['password']
       confirmpassword=request.POST['confirmpassword']

       if password == confirmpassword:
          if User.objects.filter(email=email).exists():
            messages.info(request,'email already used')
            return redirect('/register')
          elif User.objects.filter(username=username).exists():
            messages.info(request,'Username already used')
            return redirect('/register')  
          else:
            user=User.objects.create_user( username=username, email=email,password=password)
            user.save();
            return redirect('/login')
       else:
           messages.info(request, 'password not same')
           return redirect('/register') 
    else:                 
     return render(request,'register.html')

def detail(request,my_id):
    result=Video.objects.all().filter(id=my_id)
    print("south",result)

    return render(request,'detail.html',{'result':result}) 

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/index')
        else: 
            messages.info(request, 'credentials Invalid')
            return redirect ('/login')
    else:            
      return render(request,'login.html')

def profile(request):
   
    user1=Info.objects.all().filter(user=request.user)
    
    
    if request.method == "POST":
        if(user1):
            Info.objects.all().filter(user=request.user).delete()
            name=request.POST['name']
            email=request.POST['email']
            number=request.POST['number']
            gender=request.POST['gender']
           
            qualification=request.POST['qualification']
            info=Info(name=name,email=email,number=number,qualification=qualification,gender=gender,user=request.user)
            info.save()
        else:
            name=request.POST['name']
            email=request.POST['email']
            number=request.POST['number']
            gender=request.POST['gender']
        
            qualification=request.POST['qualification']
            info=Info(name=name,email=email,number=number,qualification=qualification,gender=gender,user=request.user)
            info.save()

    return render(request,'profile.html',{'user1':user1})

def logout(request):
    auth.logout(request)
    return redirect('/') 
