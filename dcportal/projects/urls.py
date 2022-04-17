from django.contrib import admin
from django.urls import path,include,re_path
from . import views

app_name='projects'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path(r'dashboard/',views.dashboard,name='dashboard'),                                       #url for dashboard
    path(r'createproject',views.createproject,name='cproject'),                                 #url for project creation
    re_path(r'^(?P<slug>[\w-]+)/$',views.project_detail,name='detail'),                         #url for project details
    # path('<slug:slug>/',views.project_detail),
]