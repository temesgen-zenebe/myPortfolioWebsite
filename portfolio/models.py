
from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
from django.urls import reverse


# Create your models here.

class Contact(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField(max_length=500 )
    created_date = models.DateTimeField('created', default=timezone.now)

    def __str__(self):
        return self.email
    

       
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=3000)
    picture = models.ImageField(upload_to="projectLogo/%Y/%m/%d" , blank=True,null=True )
    alt = models.CharField(max_length=100, blank=True ,null=True )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
class DemoImages(models.Model):
    project = models.ForeignKey(Project ,on_delete=models.CASCADE, blank=True,null=True )
    demoImages = models.ImageField(upload_to="DemoImages/%Y/%m/%d" , blank=True)
    alt = models.CharField(max_length=300, blank=True ,null=True )
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.demoImages)
        
class Languages(models.Model):
    project = models.ForeignKey(Project ,on_delete=models.CASCADE, blank=True,null=True )
    logo = models.ImageField(upload_to="LanguagesLogo/%Y/%m/%d" , blank=True)
    alt = models.CharField(max_length=100, blank=True ,null=True )
    created = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return str(self.logo)
    
class Comment(models.Model):
    project = models.ForeignKey(Project ,on_delete=models.CASCADE, blank=True,null=True )
    fistName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField(max_length=500 )
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
    
    def __str__(self):
        return str(self.fistName)