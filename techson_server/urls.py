"""techson_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from api.views import random_forest, neural_network, gradient_boosting, users, initial_data, load_image

urlpatterns = [
    url('^api/v1/random_forest/$', random_forest),
    url('^api/v1/neural_network/$', neural_network),
    url('^api/v1/gradient_boosting/$', gradient_boosting),
    url('^api/v1/users/$', users),
    url('^api/v1/init/$', initial_data),
    url('^api/v1/image/$', load_image),
]
