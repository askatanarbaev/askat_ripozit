from django.contrib import admin
from django.urls import path, include
# from accounts.views import signup
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
]
