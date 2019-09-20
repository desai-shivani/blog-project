from django.urls import path
from .views import HomeView, PostView, CreatePostView, AboutView,UpdatePostView,DeletePostView


urlpatterns = [
    path('', HomeView.as_view(),name='blog-home'),
    path('post/<int:pk>/', PostView.as_view(),name='post-detail'),
    path('create_post/', CreatePostView.as_view(),name='create-post'),
    path('about/', AboutView.as_view(),name='about'),
    path('delete_post/<int:pk>/', DeletePostView.as_view(),name='delete-post'),
    path('update_post/<int:pk>/', UpdatePostView.as_view(),name='update-post'),
]