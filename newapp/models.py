from django.db import models

# Create your models here.
class DIRECTORS(models.Model):
	dirno = models.IntegerField()
	dirname = models.CharField(max_length=25)
	dirsalary = models.IntegerField()
	dirMOVIE = models.CharField(max_length=25)
    	
