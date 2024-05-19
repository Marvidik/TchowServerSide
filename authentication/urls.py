from django.urls import path
from .views import login, register, password_reset, confirm_otp, password_reset_confirm, profile_get, profile_add, profile_delete

urlpatterns = [
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("password_reset/", password_reset, name="password_reset"),  # Updated path
    path("otp/", confirm_otp, name="confirm_otp"),
    path("resetpassword/", password_reset_confirm, name="password_reset_confirm"),
    path("profile/<int:id>/", profile_get, name="profile_get"),  # Added trailing slash and ensured `id` is `int`
    path("profile/user/add/", profile_add, name="profile_add"),
    path('profiles/<int:profile_id>/', profile_delete, name='profile_delete'),
]
