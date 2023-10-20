from django.urls import path

from user import views

urlpatterns = [
    path('test/', views.test),
    path('register/', views.register),
    path('login/', views.login),
    path('get_user_info/', views.get_user_info),
    path('get_other_user_info/', views.get_other_user_info)
]
