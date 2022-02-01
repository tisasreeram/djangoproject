from django.contrib import messages
from django.shortcuts import redirect, render
from django .http import HttpResponse
from app1.forms import SignupForm,LoginForm,UpdateForm,ChangePasswordForm
from app1.models import Signup,Pictures
from django.contrib.auth import logout as logouts
# Create your views here.
def index(request):
    a="Everyone"
    return render(request,'index.html',{'data':a})
def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']
            user=Signup.objects.filter(Email=email).exists()
            if user:
                messages.warning(request,"Email already exists")
                return redirect('/signup')
            elif password!=cpassword:
                messages.warning(request,"Password Missmatch")
                password=form.cleaned_data['Password']
                cpassword=form.cleaned_data['ConfirmPassword']
                #return redirect('/signup')
            else:
                tab=Signup(Name=name,Age=age,Place=place,Photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"Account created successfully")
                return redirect('/')
    else:
        form=SignupForm()
    return render(request,'signup.html',{'form':form})
def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            user=Signup.objects.get(Email=email)
            if not user:
                messages.warning(request,"User doesnot exist")
                return redirect('/login')
            elif password!=user.Password:
                messages.warning(request,"Password incorrect")
                return redirect('/login')
            else:
                messages.success(request,"Login Successfully")
                return redirect('/home/%s' % user.id)
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
def home(request,id):
    details=Signup.objects.get(id=id)
    return render(request,'home.html',{'details':details})
def update(request,id):
    user=Signup.objects.get(id=id)
    if request.method=="POST":
        form=UpdateForm(request.POST or None,request.FILES or None,instance=user)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['Place']
            photo=form.cleaned_data['Photo']
            email=form.cleaned_data['Email']
            #user=Signup.objects.get(id=id)
            form.save()
            messages.success(request,"Updated Successfully")
            return redirect('/home/%s' % user.id)
    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'form':form})
def changepassword(request,id):
    user=Signup.objects.get(id=id)
    if request.method=="POST":
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            cpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                messages.warning(request,"Password incorrect")
                return redirect('/changepassword/%s' %  user.id)
            elif newpassword!=cpassword:
                messages.warning(request,"Password Missmatch")
                return redirect('/changepassword/%s' % user.id)
        
            else:
                user.Password=newpassword
                user.save()
                messages.success(request,"Password changed successfully")
                return redirect('/home/%s' % user.id)
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user})
def pictures(request):
        pics=Pictures.objects.all()   
        return render(request,'pictures.html',{'pics':pics})
    
def descriptions(request,id):
    desc=Pictures.objects.get(id=id)
    return render(request,'descriptions.html',{'desc':desc})
    
def logout(request):
    logouts(request)
    messages.success(request,"Logged out successfully") 
    return redirect('/')       