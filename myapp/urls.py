from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# URL patterns for your app
urlpatterns = [
    # Public pages
    path('', views.home, name='home'),  # Home page
    path('about/', views.about, name='about'),  # About page

    # User Profile
    path('profile/', views.profile, name='profile'),

    # Blog post-related URLs
    path('create/', views.create_post, name='create_post'),  # Create a post
    path('edit/<int:pk>/', views.edit_post, name='edit_post'),  # Edit a post
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),  # Delete a post
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
    path('category/<int:category_id>/', views.category_posts, name='category_posts'),
    path('tag/<slug:tag_slug>/', views.tagged_posts, name='tagged_posts'),


    # User authentication URLs
    path('register/', views.register, name='register'),  # User registration
    path('login/', views.login_view, name='login'),  # User login
 
    # Password reset URLs (using built-in auth views)
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),  # Request password reset
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),  # Password reset done
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),  # Confirm password reset
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),  # Password reset complete

]
