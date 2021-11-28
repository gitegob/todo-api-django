from django.urls import path
from authentication.views import get_user, signup, login

urlpatterns = [
    path('signup', signup),
    path('login', login),
    path('me', get_user),
]
