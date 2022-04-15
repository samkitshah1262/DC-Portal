from django.shortcuts import render,redirect
from django.http import HttpResponse
from sqlalchemy import false

from accounts.models import User
from .models import Project
from django.contrib.auth.decorators import login_required
from dcportal.decorators import teacher_required,user_passes_test

# Create your views here.
def dashboard(request):
    projects=Project.objects.all()
    return render(request,'projects/dashboard.html',{'projects': projects })
    # return HttpResponse('samkit')

def project_detail(request,slug):
    project=Project.objects.get(slug=slug)
    return render(request,'projects/project_details.html',{ 'project': project })


@login_required(login_url='/accounts/login')
@teacher_required(login_url='/accounts/login', message='You are not authorised to perform this action.')
def createproject(request):
    if request.method=="POST":
        title = request.POST.get('title') 
        team = request.POST.get('team')
        # faculty = request.POST.get(User)
        description= request.POST.get('description')
        np=Project(title=title,team=team,faculty=request.user,description=description)
        np.save()
        return redirect('projects:dashboard')
    return render(request,'projects/create_project.html')