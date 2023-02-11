from django.urls import path, include
from .views import login_user, register_user, logout_user

urlpatterns = [
	path("", view=login_user, name='login'),
	path("register", view=register_user, name='register'),
	path("logout", view=logout_user, name='logout')
]