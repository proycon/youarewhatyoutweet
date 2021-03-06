"""yawyt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
import main

urlpatterns = [
    url(r'^$', 'main.views.twittername_entry'),
    url(r'^analyze/(?P<user>.*)$', 'main.views.analyze'),
    url(r'^results/(?P<user>.*)/(?P<classifier_name>.*)$', 'main.views.individual_classifier_result'),
    url(r'^results/(?P<user>.*)$', 'main.views.results_overview'),
    url(r'^log/(?P<user>.*)$', 'main.views.log'),
    url(r'^admin/', include(admin.site.urls)),
]
