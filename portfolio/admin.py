
from django.contrib import admin
from .models import Contact,Project,Comment,Languages,DemoImages 
  
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ('full_name','email','subject','message','created_date')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
     list_display = ('title','description','picture','alt','created','updated')
       


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['project','fistName','lastName','email','message','created']
    
@admin.register(Languages)
class LanguagesAdmin(admin.ModelAdmin):
    list_display = ['project','logo','alt','created']

@admin.register(DemoImages)
class DemoImagesAdmin(admin.ModelAdmin):
    list_display = ['project','demoImages','alt','created']