from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from django import forms
# Create your models here.

from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea


class Setting(models.Model):
    STATUS = (
        ('True ', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=25)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True,max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True,max_length=15)
    email = models.CharField(blank=True,max_length=50)
    smtpserver = models.CharField(blank=True,max_length=50)
    smtpemail = models.CharField(blank=True,max_length=50)
    smtppassword = models.CharField(blank=True,max_length=50)
    smtpport = models.CharField(blank=True,max_length=5)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(blank=True,max_length=50)
    instagram = models.CharField(blank=True,max_length=50)
    twitter = models.CharField(blank=True,max_length=50)
    aboutus = RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=10,choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title


class ContactFormMessage(models.Model):
    STATUS = (
        ('New ', 'New'),
        ('Read', 'Read'),
    )
    name = models.CharField(blank=True,max_length=100)
    email = models.CharField(blank=True,max_length=100)
    subject = models.CharField(blank=True,max_length=100)
    message = models.CharField(blank=True,max_length=100)
    status = models.CharField(max_length=10,choices=STATUS,default='New')
    ip = models.CharField(blank=True,max_length=100)
    note = models.CharField(blank=True,max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.name

class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name', 'email', 'subject','message']
        widgets = {
            'name': TextInput(attrs={'class': 'contactus','placeholder':'Name & Surname'}),
            'subject': TextInput(attrs={'class': 'contactus','placeholder':'Subject'}),
            'email': TextInput(attrs={'class': 'contactus','placeholder':'Email Address'}),
            'message': Textarea(attrs={'class': 'contactus','placeholder':'Your Message','rows':'5'}),
        }

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30,label='User name :')
    first_name = forms.CharField(max_length=50,help_text='First name',label='First name :')
    last_name = forms.CharField(max_length=50,help_text='Last name',label='Last name :')
    email = forms.EmailField(max_length=100,label='Email :')

    class Meta:
        model = User
        fields = {'username','first_name','last_name','email','password1','password2'}


