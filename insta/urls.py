from django.conf import settings
from django.conf.urls.static import static
from .views import *
from django.urls import path


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('my_profile/', my_profile, name='my_profile'),
    path('create_profile/', NewProfileView.as_view(), name='create_profile'),
    path('my_profile/create_post/', post_create, name='create_post'),
    path('my_profile/edit_profile/', edit_profile, name='edit_profile'),
    path('<int:pk>/delete/', post_delete, name='post-delete'),
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('search_posts/', search_posts, name='search_posts'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

