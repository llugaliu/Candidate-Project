from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_view.LoginView.as_view(template_name='base/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('candidate/<int:pk>/', views.candidate, name='candidate'),
    path('register-candidate/', views.register_candidate,
         name='register-candidate'),
    path('delete-candidate/<int:pk>/', views.delete_canidate, name='delete'),
    path('email/', views.email, name='email'),
    path('chat/<int:pk>/', views.chat, name='chat'),
]
