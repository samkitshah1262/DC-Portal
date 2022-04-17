from django.shortcuts import render,redirect
from django.http import HttpResponse
from sqlalchemy import false

from accounts.models import User
from .models import Project
from django.contrib.auth.decorators import login_required
from dcportal.decorators import teacher_required,user_passes_test

# Create your views here.

#function to render the html page of the dashboard
def dashboard(request):
    projects=Project.objects.all()      #stores the fetched projects from database
    return render(request,'projects/dashboard.html',{'projects': projects })        #renders page
    # return HttpResponse('samkit')

#function to render the html page of the project detail
def project_detail(request,slug):
    project=Project.objects.get(slug=slug)      #stores the fetched projects from database
    return render(request,'projects/project_details.html',{ 'project': project })       #renders page


#function to render the html page of the create project
@login_required(login_url='/accounts/login')
@teacher_required(login_url='/accounts/login', message='You are not authorised to perform this action.')
def createproject(request):
    if request.method=="POST":                                # if page is getting a post request thst isd form is filled
        title = request.POST.get('title') 
        team = request.POST.get('team')
        # faculty = request.POST.get(User)
        description= request.POST.get('description')
        np=Project(title=title,team=team,faculty=request.user,description=description)      #creates project of class Project
        np.save()                                             #saves it in database
        return redirect('projects:dashboard')               #redirects to dashboard page
    return render(request,'projects/create_project.html')           #renders page