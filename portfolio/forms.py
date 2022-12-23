from dataclasses import field
from tkinter import Widget
from django.forms import ModelForm,Textarea
from .models import Contact ,Comment

    
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name','email','subject','message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 4}),
        }
        labels = {
            'email': "Email",
        }
        
class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('fistName','lastName','email','message')
        widgets = {
            'message': Textarea(attrs={'cols': 30, 'rows': 4}),
        }
        labels = {
            'email': "Email",
        }
        
