from django.urls import path
from . import views
from .views import (PostListView, PostDetailView, PostUpdateView, PostCreateView, PostDeleteView, UserPostListView)


urlpatterns = [
    
    path('', PostListView.as_view(), name='user-home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='User-post'),
    path('about.html/', views.about, name='About Us'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='Post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='Post-update'),
    path('post/new/', PostCreateView.as_view(), name='Post-create'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='Post-delete')
]