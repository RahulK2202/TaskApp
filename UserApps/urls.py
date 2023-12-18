from django.urls import path
from.import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('',views.LoginUserView.as_view(),name='user-login'),
    path('register/', views.RegisterUserView.as_view(), name='user-register'),
    path('otp/',views.OtpUserView.as_view(),name='user-otp'),
    path('home/',views.UserHome,name='user-home'),
    path('logout/',views.logout,name='user-logout'),

]  