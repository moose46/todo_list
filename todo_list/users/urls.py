from django.urls import path
# from django.contrib.auth.views import LogoutView
from .views import MyLoginView, RegisterView,PatchLogoutView
from django.contrib.auth.views import (
    LogoutView, 
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

urlpatterns = [
    path('login/', MyLoginView.as_view(),name='login'),
    # path('logout/', LogoutView.as_view(),name='logout'),
    # https://github.com/encode/django-rest-framework/issues/9206
    path('logout/', PatchLogoutView.as_view(),name='logout'),
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/', PasswordResetView.as_view(template_name='users/password_reset.html'),name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),

]
