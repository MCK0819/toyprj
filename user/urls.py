from django.conf.urls import include
# from .views import joinView
from django.views.decorators.csrf import csrf_exempt

from user.views import idconfirm
from rest_framework import routers
from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('join', views.join, name='join'),
    path('idconfirm', views.idconfirm, name='idconfirm'),
    path('emailconfirm', views.emailconfirm, name='emailconfirm'),
    path('log_in', views.log_in, name='log_in'),
    path('log_out', views.log_out, name='log_out'),
    # path('log_in', auth_views.LoginView.as_view(template_name='main.html'), name='log_in'),
]