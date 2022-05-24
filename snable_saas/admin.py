from django.contrib import admin
from .models import Brochure, Contact_genral_form, Contact_training_hiring_form, Services, SubServices, Post, BlogComment, Positions, CareerApplications
# Register your models here.

# admin.site.register(Brochure)
@admin.register(Brochure)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','title','docs']

# admin.site.register(Contact_genral_form)
@admin.register(Contact_genral_form)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','full_name','company_name','designation','email','services','sub_services','mobile_number','whatsapp_number','message']

# admin.site.register(Contact_training_hiring_form)
@admin.register(Contact_training_hiring_form)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','full_name', 'qualification', 'email', 'mobile_number', 'whatsapp_number', 'message']

# admin.site.register(Services)
@admin.register(Services)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','services_name']

# admin.site.register(SubServices)
@admin.register(SubServices)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','services_name', 'sub_services_name']

# admin.site.register(Post)
@admin.register(Post)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','title', 'description', 'body']

# admin.site.register(Post)
@admin.register(BlogComment)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','comment', 'name', 'email', 'post', 'timestamp']

# admin.site.register(Positions)
@admin.register(Positions)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','position', 'description', 'status']

# admin.site.register(CareerApplications)
@admin.register(CareerApplications)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['id','full_name', 'email', 'number', 'position_applied_for', 'uploaded_cv']