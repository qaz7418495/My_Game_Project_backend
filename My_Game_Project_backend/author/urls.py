from django.urls import path

from author import views

urlpatterns = [
    path('index/', views.index),
    path('get_user_list/', views.get_user_list),
    path('add_user/', views.add_user),
]
