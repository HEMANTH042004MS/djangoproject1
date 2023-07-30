from django.contrib import admin
from newapp.models import DIRECTORS

# Register your models here.
class directorsadmin(admin.ModelAdmin):
	list = ['dirno','dirname','dirsalary','dirMOVIE']
admin.site.register(DIRECTORS,directorsadmin)
