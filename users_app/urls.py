from django.urls import path
from users_app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login', views.user_login, name="login"),
    path('logout', auth_views.LogoutView.as_view(
        template_name='logout.html'), name='logout'),
]
