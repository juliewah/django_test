"""mysite URL Configuration

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
from django.urls import path, re_path, include
from trips.views import home, showImg, post_detail, post_new, post_delete, post_edit, register
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home), #首頁
    path('showImg/', showImg),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', register, name='register'),
    path('', include('social_django.urls', namespace='social')),
    re_path(r'^post/(?P<pk>\d+)/$', post_detail, name="post_detail"),
    re_path(r'^post/new/$', post_new, name='post_new'),
    re_path(r'^post/(?P<pk>[0-9]+)/delete/$', post_delete, name='post_delete'),
    re_path(r'^post/(?P<pk>[0-9]+)/edit/$', post_edit, name='post_edit'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)