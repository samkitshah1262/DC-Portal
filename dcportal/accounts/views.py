# from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# # Create your views here.

# def signup_view(request):
#     form = UserCreationForm()
#     return render(request,'accounts/signup.html',{'form':form})

from accounts.models import user_type
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from accounts.models import user_type, User

def signup(request):
    if (request.method == 'POST'):
        email = request.POST.get('email')
        password = request.POST.get('password')
        st = request.POST.get('student')
        te = request.POST.get('teacher')
        
        user = User.objects.create_user(
            email=email,
        )
        user.set_password(password)
        user.save()
        
        usert = None
        if st:
            usert = user_type(user=user,is_student=True)
        elif te:
            usert = user_type(user=user,is_teach=True)
        
        usert.save()
        #Successfully registered. Redirect to homepage
        return redirect('accounts:login')
    # return render(request,'/accounts/signup.html')
    return render(request,'accounts/signup.html')
    # return HttpResponse('samkit')
    
def login(request):
    if (request.method == 'POST'):
        email = request.POST.get('email') #Get email value from form
        password = request.POST.get('password') #Get password value from form
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.is_student:
                return redirect('accounts:shome') #Go to student home
                # return HttpResponse('samkit')
                # return render(request,'accounts/student_home.html')
            elif user.is_authenticated and type_obj.is_teach:
                return redirect('accounts:thome') #Go to student home
                # return render(request,'accounts/teacher_home.html') #Go to teacher home
        else:
            # Invalid email or password. Handle as you wish
            return redirect('accounts:login')

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method=='POST':
        auth_logout(request)
        return redirect('accounts:login')

def shome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return render(request,'accounts/student_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return redirect('accounts:thome')
    else:
        return redirect('accounts:login')
                      
def thome(request):
    if request.user.is_authenticated and user_type.objects.get(user=request.user).is_teach:
        return render(request,'accounts/teacher_home.html')
    elif request.user.is_authenticated and user_type.objects.get(user=request.user).is_student:
        return redirect('accounts:shome')
    else:
        return redirect('accounts:home')