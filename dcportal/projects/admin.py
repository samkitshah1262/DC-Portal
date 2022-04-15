from django.contrib import admin
from .models import Project, Teacher, Student


# Register your models here.
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user',)

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user',)

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)

admin.site.register(Project)