from django.urls import path
from .views import UsersAPIView, UserDetailView, UserListView

urlpatterns = [
    path('api/create/', UsersAPIView.as_view(), name='create_user'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/search/', UserListView.as_view(), name='user-list'),
]