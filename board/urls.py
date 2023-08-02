from board import views
from django.urls import path

urlpatterns = [
    # path('get_data', views.getData, name='get_data'),
    path('board_detail/<int:pk>', views.board_Detail, name='board_detail'),
    path('board_create', views.board_create, name='board_create'),
    path('board_edit/<int:pk>', views.board_Edit, name='board_edit'),
    path('board_delete/<int:pk>', views.board_delete, name='board_delete'),
    path('like/<int:pk>', views.like, name='like'),
]