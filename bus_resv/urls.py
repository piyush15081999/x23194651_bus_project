"""
URL configuration for bus_resv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.loginx, name='loginx'),
    path('handle_login/', views.handle_login, name='handle_login'),
    path('signup/', views.signup, name='signup'),
    path('handle_signup/', views.handle_signup, name='handle_signup'),
    path('buses/', views.buses, name='buses'),
    path('book_bus/', views.book_bus, name='book_bus'),
    path('handle_book_bus/', views.handle_book_bus, name='handle_book_bus'),
    path('booked_bus/', views.booked_bus, name='booked_bus'),
    path('edit_booking/', views.edit_booking, name='edit_booking'),
    path('handle_edit_booking/', views.handle_edit_booking, name='handle_edit_booking'),
    path('delete_booking/', views.delete_booking, name='delete_booking'),
    path('my_logout/', views.my_logout, name='my_logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
