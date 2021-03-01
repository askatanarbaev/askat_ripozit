from django.contrib import admin
from django.urls import path, include
from accounts.views import signup
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('admin/', admin.site.urls),
    path('', include('insta.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
