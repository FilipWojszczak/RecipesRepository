from django.urls import path, re_path
from .views import signup, account_activation_sent, activate, PasswordResetCompleteView, PasswordResetConfirmView



urlpatterns = [
    path('signup/', signup, name='signup'),
    re_path(r'^account_activation_sent/$', account_activation_sent, name='account_activation_sent'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,40})/$', activate, name='activate'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
