from django.urls import path
from users.views import HomeView, SignUpView

from . import views

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    
]