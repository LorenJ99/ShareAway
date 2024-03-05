from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('idea/<int:pk>', views.idea, name="idea"),
    path('delete_idea/<int:pk>', views.delete_idea, name='delete_idea'),
    path('add_idea/', views.add_idea, name='add_idea'),
    path('update_idea/<int:pk>', views.update_idea, name='update_idea'),
]