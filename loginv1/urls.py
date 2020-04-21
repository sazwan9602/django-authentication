from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from . import views
"""
    #by default loginView/logoutView will look at registration dir, you can change the dir by define your path in
    as_view(template_name='YOUR/TEMPLATE/PATH')

"""

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='registerv1'),
    path('profile/', views.profile, name='profilev1'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
                                                redirect_authenticated_user=True), name='loginv1'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logoutv1'),

    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='authentication/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='authentication/password_change.html',
        success_url=reverse_lazy('password_change_done')
    ), name='password_change'),

    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='authentication/password_reset.html',
        # success_url=reverse_lazy('password_reset_confirm')
    ), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='authentication/password_reset_done.html',
    ), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='authentication/password_reset_confirm.html',
    ), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='authentication/password_reset_complete.html'), name='password_reset_complete')

]