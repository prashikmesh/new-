from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField
from django.utils.timezone import now

# Create your models here.
class Brochure(models.Model):
    title = models.CharField(max_length=100)
    docs = models.FileField(upload_to='book/docs')

class Contact_genral_form(models.Model):
    full_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    services = models.CharField(max_length=50, default=None)
    sub_services = models.CharField(max_length=50, default=None)
    mobile_number = models.BigIntegerField()
    whatsapp_number = models.BigIntegerField()
    message = models.CharField(max_length=200)

class Contact_training_hiring_form(models.Model):
    full_name = models.CharField(max_length=100)
    qualification = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    mobile_number = models.BigIntegerField()
    whatsapp_number = models.BigIntegerField()
    message = models.CharField(max_length=200)

class Services(models.Model):
    services_name = models.CharField(max_length=100)

class SubServices(models.Model):
    services_name = models.IntegerField()
    sub_services_name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    # description = RichTextField(blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    slug = models.CharField(max_length=150)

class BlogComment(models.Model):
    comment = models.TextField()
    name = models.CharField(max_length=220)
    email = models.EmailField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=now)
    # This is text choice where you can at least two values ON/OFF BLOCK/UNBLOCK
    employeStatus = models.TextChoices('employeStatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', max_length=20, choices=employeStatus.choices)

class Positions(models.Model):
    position = models.CharField(max_length=250, blank=True, null=True)
    description = RichTextUploadingField(blank=True, null=True)
    employeStatus = models.TextChoices('employeStatus', 'BLOCK UNBLOCK')
    status = models.CharField(default='BLOCK', max_length=20, choices=employeStatus.choices)

class CareerApplications(models.Model):
    full_name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField()
    number = models.BigIntegerField()
    position_applied_for = models.CharField(max_length=150, blank=True, null=True)
    uploaded_cv = models.FileField(upload_to='book')


