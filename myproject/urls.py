from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView

# Main URL configuration
urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # App URLs
    path('', include('myapp.urls')),  # Includes URLs from my app

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Default Django auth views
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),

]
