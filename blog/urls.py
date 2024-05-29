from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  re_path(r'^$', views.post_list, name='post_list'),
  re_path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
  re_path(r'^post/new/$', views.post_new, name='post_new'),
  re_path(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)