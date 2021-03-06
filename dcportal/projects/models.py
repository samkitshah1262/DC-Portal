from curses import termname
from datetime import date
from re import template
from django.db import models
from jupyterlab_server import slugify
from matplotlib.pyplot import title
from tables import Description
from accounts.models import User
# Create your models here.

class Project(models.Model):                            #project model
    title=models.CharField(max_length=100)              
    slug=models.SlugField()
    faculty=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    # date=models.DateTimeField(auto_now_add=True)
    team=models.IntegerField()
    # vacancy=models.BooleanField()
    appliedstudents=models.CharField(max_length=500,default='',blank=True)
    acceptedstudents=models.CharField(max_length=500,default='',blank=True)
    description=models.TextField()


    def __str__(self):
        return self.title

class Teacher(models.Model):                                        #teacher model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    floated_projects = models.ManyToManyField(Project, related_name='floated_projects', blank=True)            #many to many field because muliple students can apply to multiple projects
    requested_projects = models.ManyToManyField(Project, related_name="requested_projects", blank=True)         #many to many field because muliple students can apply to multiple projects

class Student(models.Model):                                            #student model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    applied_projects = models.ManyToManyField(Project, related_name="applied_projects", blank=True)         #many to many field because muliple students can apply to multiple projects
    accepted_projects = models.ManyToManyField(Project, related_name="accepted_projects", blank=True)       #many to many field because muliple students can apply to multiple projects