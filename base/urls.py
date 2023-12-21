from django.urls import path

from base import views

urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutuser, name='logout'),
    path('register/', views.registerPage, name='register'),
    path('', views.home, name='home'),
    path('rooms/<str:pk>/', views.rooms, name='rooms'),
    path('profile/<str:pk>/', views.user_profile, name='user_profile'),
    path('create_room/', views.create_room, name='create_room'),
    path('update_room/<str:pk>/', views.update_room, name='update_room'),
    path('delete_room/<str:pk>/', views.delete_room, name='delete_room'),
    path('delete_message/<str:pk>/', views.delete_message, name='delete_message'),
    path('update_user/', views.update_user, name='update_user'),
    path('topics/', views.topic_page, name='topics'),
    path('activity/', views.activity_page, name='activity'),
]