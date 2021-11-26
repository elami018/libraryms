"""librarymanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from library import views
from django.contrib.auth.views import LoginView,LogoutView
#from django-email-verification import email_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls') ),
    path('', views.home_view),
#     path('admin/', admin.site.urls),
#     path('email/', include(email_urls)),

    path('adminclick', views.adminclick_view),
    path('studentclick', views.studentclick_view),


    path('adminsignup', views.adminsignup_view),
    path('studentsignup', views.studentsignup_view),

    path('adminlogin', LoginView.as_view(template_name='library/adminlogin.html')),
    path('studentlogin', LoginView.as_view(template_name='library/studentlogin.html'),name='studentlogin'),

    path('logout', LogoutView.as_view(template_name='library/index.html')),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),

    path('addbook', views.addbook_view),
    path('viewbook', views.viewbook_view,name = 'viewbook'),
    path('issuebook', views.issuebook_view),
    path('viewissuedbook', views.viewissuedbook_view),
    path('viewstudent', views.viewstudent_view),
    path('viewissuedbookbystudent', views.viewissuedbookbystudent),
    path('viewbooks', views.viewissuedbookbystudent),

    path('BooksAvailable', views.booksAvailable_view),
   # path('deleteRecords',views.deleteRecords),


    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view),
    path('userbooklog/<str:username>', views.userbooklog, name='userbooklog'),
    path('modifybook/<str:isbn>', views.modifybook, name='modifybook'),
    path('deletebook/<str:isbn>', views.deletebook, name='deletebook'),
    path('RenewBook/<str:borrowerID>/', views.RenewBook, name='RenewBook'),
    path('ComingUp', views.ComingUp, name='ComingUp'),
    path('CloseToDeadline', views.CloseToDeadline, name='CloseToDeadline'),
    path('activate/<uidb64>/<token>',views.VerificationEmail, name = 'activate'),
    path('userhistory', views.userhistory),
    path('searchbooksadmin', views.searchbooksadmin, name = "searchbooksadmin"),
    path('searchbookrequests', views.searchbookrequests, name = "searchbookrequests"),
    path('searchstudent', views.searchstudent, name = "searchstudent"),
    path('searchbooksavailable', views.searchbooksavailable, name = "searchbooksavailable"),
]
