from django.urls import path
from authentication.views import Login, Signup, GetUser

urlpatterns = [
    path('signup', Signup.as_view()),
    path('login', Login.as_view()),
    path('me', GetUser.as_view()),
]
