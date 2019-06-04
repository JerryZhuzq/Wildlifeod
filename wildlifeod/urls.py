"""wildlifeod URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from monitorsys import views as monitorsys_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',monitorsys_views.login),
    url(r'^index/',monitorsys_views.index, name = "index"),
    url(r'^upload_img/', monitorsys_views.upload_img, name = "upload_img"),
    url(r'^upload_video/', monitorsys_views.upload_video, name = "upload_video"),
    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)