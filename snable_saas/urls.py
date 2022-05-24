from django.urls import path, include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.loadHomeScreen, name='home'),
    path('aboutus', views.loadAboutUs, name='aboutus'),
    path('traininghiring', views.loadTraningAndPlacement, name='traininghiring'),

    path('trainingandhiringuiux', views.loadTrainingAndHiringUiUx, name='trainingandhiringuiux'),

    path('digitalmarketing', views.loadDigitalMarketing, name='digitalmarketing'),
    path('webappdevelopment', views.loadWebAndAppDevelopment, name='webappdevelopment'),
    path('virtualassistance', views.loadVirtualAssistance, name='virtualassistance'),
    path('faq', views.loadFAQ, name='faq'),
    path('privacypolicy', views.loadPrivacyPolicy, name='privacypolicy'),

    path('insert_post_comments', views.postComment),

    path('blog', views.loadMainBlog, name='blog'),
    path('blogreadmore/<int:bid>', views.loadBlogReadMore, name='blogreadmore'),


    # url for insert records
    path('insert_general_form', views.insertGeneralFromRecord),
    path('insert_training_hiring_form', views.insertTrainingHiringFromRecord),
    # Admin url
    path('admin', views.loadAdminPanelLogin),
    path('admin_login', views.adminLogin),
    path('admin_logout', views.adminLogout, name='admin_logout'),
    path('admin_panel_general_contact', views.loadAdminGeneralContact, name='admin_panel_general_contact'),
    path('admin_panel_student_contact', views.loadAdminStudentContact, name='admin_panel_student_contact'),
    # get sub services url
    path('get_sub_services', views.getSubServices),

    # Admin Blog Dashboard urls
    path('admin_blog_dashboard',views.loadAdminBlogDashboard, name='admin_blog_dashboard'),
    path('add_blog_form', views.loadAddBlogForm, name='add_blog_form'),
    path('view_all_blog', views.loadViewAllBlog, name='view_all_blog'),
    path('delete_blog/<int:bid>', views.deleteBlog, name='delete_blog'),
    path('edit_blog/<int:bid>', views.editBlog, name='edit_blog'),
    path('ckeditor', include('ckeditor_uploader.urls')), # blog media file upload using this method.
    path('admin_blog_comments', views.loadAdminBlogComments, name='admin_blog_comments'),
    path('blog_comment_status/<int:bcid>/<str:bcst>', views.BlogCommentStatusFunction, name='blog_comment_status'),

    # Career Dashboard
    path('career_home_page', views.loadCareerHomePage, name='career_home_page'),
    path('add_position', views.loadAdminAddPosition, name='add_position'),
    path('show_all_positions',views.loadViewAllPositions, name='show_all_positions'),
    path('position_status/<int:pid>/<str:pst>', views.positionStatusFunction, name='position_status'),
    path('delete_position_record/<int:pid>', views.deletePositionsRecord, name='delete_position_record'),
    path('edit_position/<int:pid>', views.editPosition, name='edit_position'),
    path('show_all_applications', views.loadAllApplications, name='show_all_applications'),
    path('insert_applications', views.insertApplication, name='insert_applications'),

    # Career
    path('career', views.loadCareer, name='career'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)