from django.db import models

# Create your models here.

from ckeditor_uploader.fields import RichTextUploadingField


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
         return self.title

