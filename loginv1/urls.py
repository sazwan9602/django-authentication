from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
"""
    #by default loginView/logoutView will look at registration dir, you can change the dir by define your path in
    as_view(template_name='YOUR/TEMPLATE/PATH')

"""
app_name = 'authv1'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='registerv1'),
    path('profile/', views.profile, name='profilev1'),
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html', redirect_authenticated_user=True), name='loginv1'),
    path('logout/', auth_views.LogoutView.as_view(template_name='authentication/logout.html'), name='logoutv1')

]