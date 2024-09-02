from django.urls import path, include
from dj_rest_auth.views import LoginView
from accounts.views import RegisterView
urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    # path('register/', include('dj_rest_auth.registration.urls'), name='register'),
    path('register/', RegisterView.as_view(), name='register'),
]