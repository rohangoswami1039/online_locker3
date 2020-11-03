from django.http import HttpResponse 
from django.shortcuts import render 

# Create your views here.
#home page
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request,'login.html')
def sign_up(request):
    return render(request,'sign_up.html')
def user_sign_up(request):
    sign_user_name=request.POST['sign_username']
    sign_password=request.POST['sign_password']
    sign_userid=request.POST['sign_userid']
    if sign_user_name=="" or sign_userid=="" or sign_password=="":
        return HttpResponse("Can't create the User id please try again ")
    return render(request,'user_signup.html')

def user_login(request):
    log_submit_username=request.POST['user_name']
    log_submit_password=request.POST['password']
    if log_submit_username=="" or log_submit_password=="":
        return HttpResponse("Please Enter the user id or password ")
    return render(request,'user_login.html')