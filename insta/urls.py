from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('my_profile/', my_profile, name='my_profile'),
    path('create_profile', NewProfileView.as_view(), name='create_profile'),
    path('my_profile/create_post/', post_create, name='create_post')

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

