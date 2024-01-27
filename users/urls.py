from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_view
from .views import signup_view

urlpatterns = [
    path('signup/', user_view.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
]
