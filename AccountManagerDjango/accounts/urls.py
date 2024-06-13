from django.urls import path
from .views import UsersAPIView

urlpatterns = [
    path('create/', UsersAPIView.as_view(), name='create_user'),
]