from django.shortcuts import render, redirect
//aruna dilo ki shooter hai mera scooter
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User, auth
from .models import Brochure, Contact_genral_form, Contact_training_hiring_form, Services, SubServices, Post, BlogComment, Positions, CareerApplications
from .forms import PostForm, PositionForm
# Create your views here.

# -- Get Sub services URLS --
def getSubServices(request):
    vservices = request.GET.get('services') # name attribute to select tag
    vsub_services = SubServices.objects.filter(services_name=vservices)
    return render(request,'get-sub-services.html', {'result':vsub_services})


# -- load home screen page --
def loadHomeScreen(request):
    obj = Services.objects.all()
    return render(request, 'home-screen.html', {'results': obj})

# -- load about us page --
def loadAboutUs(request):
    obj = Services.objects.all()
    return render(request, 'about-us.html', {'results': obj})

# -- load traning and placement page --
def loadTraningAndPlacement(request):
    obj = Brochure.objects.all()
    return render(request, 'training-and-placement.html', {'result':obj})

# -- load training and hiring UI / UX Page --
def loadTrainingAndHiringUiUx(request):
    return render(request, 'training-and-hiring-ui-ux.html')

# -- load digital marketing --
def loadDigitalMarketing(request):
    obj = Services.objects.all()
    return render(request, 'digital-marketing.html', {'results': obj})

# -- load Web & App Development --
def loadWebAndAppDevelopment(request):
    obj = Services.objects.all()
    return render(request, 'web-app-development.html', {'results': obj})

# -- load virtual assistance --
def loadVirtualAssistance(request):
    obj = Services.objects.all()
    return render(request, 'virtual-assistance.html', {'results': obj})

# -- load FAQ Page --
def loadFAQ(request):
    obj = Services.objects.all()
    return render(request, 'faq.html', {'results': obj})

# -- load Privacy Policy Page --
def loadPrivacyPolicy(request):
    return render(request, 'privacy-policy.html')

# -- load Blog Page --
def loadMainBlog(request):
    obj = Services.objects.all()
    obj_p = Post.objects.all()
    return render(request,'blogs-main.html',{'results':obj, 'result1':obj_p})

# -- load Blog Read More Page --
def loadBlogReadMore(request,bid):
    obj = Services.objects.all()
    obj1 = Post.objects.get(id=bid)
    obj_comment = BlogComment.objects.filter(post=obj1, status='UNBLOCK')
    return render(request,'blog-read-more.html',{'results':obj,'result':obj1, 'obj_comments':obj_comment})


# -- Insert Genral form Record --
def insertGeneralFromRecord(request):
    if request.method == 'POST':
        vfull_name = request.POST.get('full_name')
        vcompany_name = request.POST.get('company_name')
        vdesignation = request.POST.get('designation')
        vemail_id = request.POST.get('email_id')
        vservices = request.POST.get('services')
        vsub_services = request.POST.get('sub_services')
        vmobile_number = request.POST.get('mobile_number')
        vwhatsapp_number = request.POST.get('whatsapp_number')
        vmessage = request.POST.get('message')

        name = "Name:" + vfull_name
        company_name = "Company Name:" + vcompany_name
        designation = "Designation:" + vdesignation
        email = "Email ID:" + vemail_id
        #  Get services name using id.
        services_obj = Services.objects.get(id=vservices)
        services = "Services:" + services_obj.services_name
        #   Get sub services name  using id.
        sub_services_obj = SubServices.objects.get(id=vsub_services)
        sub_services = "Sub Services:" + sub_services_obj.sub_services_name
        mobile_number = "Mobile Number:" + vmobile_number
        whatsapp_number = "Whatsapp Number:" + vwhatsapp_number
        message1 = "Message:" + vmessage

        send_mail(
            'New admission',  # Subject here
            name + "\n" + company_name + "\n" + designation + "\n" + email + "\n" + services + "\n" + sub_services + "\n" + mobile_number + "\n" + whatsapp_number + "\n" + message1, # Here is the message.
            settings.EMAIL_HOST_USER,  # from@example.com
            ['ankit200p@gmail.com'],  # to@example.com
            fail_silently=False,
        )

        obj = Contact_genral_form()
        obj.full_name = vfull_name
        obj.company_name = vcompany_name
        obj.designation = vdesignation
        obj.email = vemail_id
        obj.services = vservices
        obj.sub_services = vsub_services
        obj.mobile_number = vmobile_number
        obj.whatsapp_number = vwhatsapp_number
        obj.message = vmessage
        obj.save()
        messages.success(request, 'Your Contact Submit successfully....')
        return redirect('/')
    else:
        return redirect('/')

# -- Insert Training and hiring form Record --
def insertTrainingHiringFromRecord(request):
    if request.method == 'POST':
        vfull_name = request.POST.get('full_name')
        vqualifications = request.POST.get('qualifications')
        vemail_id = request.POST.get('email_id')
        vmobile_number = request.POST.get('mobile_number')
        vwhatsapp_number = request.POST.get('whatsapp_number')
        vmessage = request.POST.get('message')

        name = "Name:" + vfull_name
        qualification = "Qualification:" + vqualifications
        email = "Email ID:" + vemail_id
        mobile_number = "Mobile Number:" + vmobile_number
        whatsapp_number = "Whatsapp Number:" + vwhatsapp_number
        message1 = "Message:" + vmessage

        send_mail(
            'New admission', # Subject here
            name + "\n" + qualification + "\n" + email + "\n" + mobile_number + "\n" + whatsapp_number + "\n" + message1, #Here is the message.
            'snablein@gmail.com', #from@example.com
            ['ankit200p@gmail.com'], #to@example.com
            fail_silently=False,
        )

        obj = Contact_training_hiring_form()
        obj.full_name = vfull_name
        obj.qualification = vqualifications
        obj.email = vemail_id
        obj.mobile_number = vmobile_number
        obj.whatsapp_number = vwhatsapp_number
        obj.message = vmessage
        obj.save()
        messages.success(request, 'Your Contact Submit ....')
        return redirect('/traininghiring')
    else:
        return redirect('/traininghiring')

# --- Admin Panel ---
# -- Load admin login page --
def loadAdminPanelLogin(request):
    return render(request, 'admin-login.html')

# -- Admin Login --
def adminLogin(request):
    if request.method=='POST':
        vusername = request.POST.get('uname')
        vpassword = request.POST.get('pswd')
            # It will match the contents of the textbox from the table fields
        myuser = auth.authenticate(username=vusername,password=vpassword)

        if myuser is not None:
            auth.login(request,myuser)
            return redirect('/admin_panel_general_contact')
        else:
            messages.success(request, 'Invalid Username and Password...')
            return redirect('/admin')

# -- Admin Logout --
def adminLogout(request):
    auth.logout(request)
    return redirect('/admin')

# -- Load admin general contact --
def loadAdminGeneralContact(request):
    if request.user.is_authenticated:
        obj = Contact_genral_form.objects.raw("SELECT snable_saas_contact_genral_form.id,snable_saas_contact_genral_form.full_name,snable_saas_contact_genral_form.company_name,snable_saas_contact_genral_form.designation,snable_saas_contact_genral_form.email, snable_saas_contact_genral_form.mobile_number,snable_saas_contact_genral_form.whatsapp_number,snable_saas_contact_genral_form.message,snable_saas_services.services_name,snable_saas_subservices.sub_services_name FROM snable_saas_contact_genral_form LEFT JOIN snable_saas_services ON (snable_saas_contact_genral_form.services = snable_saas_services.id)LEFT JOIN snable_saas_subservices ON snable_saas_contact_genral_form.sub_services=snable_saas_subservices.id")
        return render(request, 'admin-general-contact.html', {'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')


# -- Load admin general contact --
def loadAdminStudentContact(request):
    if request.user.is_authenticated:
        obj = Contact_training_hiring_form.objects.all()
        return render(request, 'admin-student-contact.html', {'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Load Admin Blog --
def loadAdminBlogDashboard(request):
    if request.user.is_authenticated:
        obj = Post.objects.all()
        return render(request, 'admin-blog-dashboard.html',{'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Load Add blog form --
def loadAddBlogForm(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/view_all_blog')
        else:
            form = PostForm()
        return render(request, 'admin-add-blog.html', {'form':form})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Load view all blog  --
def loadViewAllBlog(request):
    if request.user.is_authenticated:
        obj = Post.objects.all()
        return render(request, 'admin-view-all-blog.html',{'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# --- Delete Blog ---
def deleteBlog(request,bid):
    obj = Post.objects.get(id=bid) #get a particular record
    obj.delete()
    return redirect('/view_all_blog')

# --- Edit Blog ---
def editBlog(request,bid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Post.objects.get(id=bid)
            form = PostForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('/view_all_blog')
        else:
            obj = Post.objects.get(id=bid)
            form = PostForm(instance=obj)
        return render(request, 'admin-edit-blog.html', {'form':form})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Post Blogs Comments --
def postComment(request):
    if request.method == "POST":
        vcomment = request.POST.get("ecomment")
        vname = request.POST.get("ename")
        vemail = request.POST.get("eemail")
        vpostid = request.POST.get("epostid")
        vpost = Post.objects.get(id=vpostid)

        name = "Name:" + vname
        comment = "Comment:" + vcomment

        send_mail(
            'New Comment',  # Subject here
            name + "\n" + comment,
            # Here is the message.
            'snablein@gmail.com',  # from@example.com
            ['ankit200p@gmail.com'],  # to@example.com
            fail_silently=False,
        )


        obj = BlogComment()
        obj.comment = vcomment
        obj.name = vname
        obj.email = vemail
        obj.post = vpost
        obj.save()
        return redirect(f'blogreadmore/{vpostid}')

# -- View All blog comments --
def loadAdminBlogComments(request):
    obj = BlogComment.objects.all()
    return render(request, 'admin-blog-comment.html', {'result':obj})

# -- Blog Comment Status --
def BlogCommentStatusFunction(request,bcid,bcst):
    if (bcst=='BLOCK'):
        obj = BlogComment.objects.get(id=bcid)
        obj.status='UNBLOCK'
        obj.save()
        return redirect('/admin_blog_comments')
    else:
        obj = BlogComment.objects.get(id=bcid)
        obj.status = 'BLOCK'
        obj.save()
        return redirect('/admin_blog_comments')

# -- django error handler --
def handler400(request, exception):
    return render(request, "400.html", status=400)

def handler403(request, exception):
    return render(request, "403.html", status=403)

def handler404(request, exception):
    return render(request, "404.html", status=404)

def handler500(request):
    return render(request, "500.html", status=500)

# -- Career --
# -- Load career home page for dashboard --
def loadCareerHomePage(request):
    if request.user.is_authenticated:
        obj = CareerApplications.objects.all()
        return render(request, 'admin-career-dashboard.html', {'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')


# -- Load Admin add position file --
def loadAdminAddPosition(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PositionForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('/show_all_positions')
        else:
            form = PositionForm()
        return render(request, 'admin-add-position.html', {'form':form})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Load Show all Position  --
def loadViewAllPositions(request):
    if request.user.is_authenticated:
        obj = Positions.objects.all()
        return render(request, 'admin-view-all-positions.html',{'result':obj})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- Position Status Options --
def positionStatusFunction(request,pid,pst):
    if (pst=='BLOCK'):
        obj = Positions.objects.get(id=pid)
        obj.status='UNBLOCK'
        obj.save()
        return redirect('/show_all_positions')
    else:
        obj = Positions.objects.get(id=pid)
        obj.status = 'BLOCK'
        obj.save()
        return redirect('/show_all_positions')

# --- Delete Positions ---
def deletePositionsRecord(request,pid):
    obj = Positions.objects.get(id=pid) #get a particular record
    obj.delete()
    return redirect('/show_all_positions')

# --- Edit Positions ---
def editPosition(request,pid):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = Positions.objects.get(id=pid)
            form = PositionForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
                return redirect('/show_all_positions')
        else:
            obj = Positions.objects.get(id=pid)
            form = PositionForm(instance=obj)
        return render(request, 'admin-edit-positions.html', {'form':form})
    else:
        messages.success(request, 'Please Login first...')
        return redirect('/admin')

# -- load all applications in admin --
def loadAllApplications(request):
    obj = CareerApplications.objects.all()
    return render(request,'admin-show-applications.html', {'result':obj})

# -- Submit application for position --
def insertApplication(request):
    if request.method == 'POST':
        vfull_name = request.POST.get('full_name')
        vemail = request.POST.get('email')
        vnumber = request.POST.get('number')
        vposition_apply = request.POST.get('position_apply')
        vuploaded_cv = request.FILES['bdocs']

        obj = CareerApplications()
        obj.full_name = vfull_name
        obj.email = vemail
        obj.number = vnumber
        obj.position_applied_for = vposition_apply
        obj.uploaded_cv = vuploaded_cv

        obj.save()
        return redirect('/career')
    else:
        return redirect('/career')

# -- load career page --
def loadCareer(request):
    obj = Positions.objects.filter(status='UNBLOCK')
    return render(request,'career.html', {'result':obj})



