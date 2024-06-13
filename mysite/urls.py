
from django.contrib import admin
from django.urls import include, re_path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.authtoken import views


urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'', include('blog.urls')),
    re_path(r'^api-token-auth/', obtain_auth_token),
]
