from django.urls import path
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)


urlpatterns = [
    path('password_reset', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password_reset_complete', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
