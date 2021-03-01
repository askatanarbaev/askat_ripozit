from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('my_profile/', my_profile, name='my_profile')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
