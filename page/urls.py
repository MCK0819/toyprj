from django.conf.urls import url
from page import views
from django.urls import path

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('main/', views.go_main, name='main'),
    path('board_reg', views.board_reg, name='board_reg'),
    path('board_update/<int:pk>', views.board_update, name='board_update'),
]
