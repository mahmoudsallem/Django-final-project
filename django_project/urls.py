"""
URL configuration for django_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from .views import landing_page
from about.views import about_page

urlpatterns = [
    path('', landing_page, name='hotel-landingpage'),
    path('about/', about_page, name='about_page'),
    path('admin/', admin.site.urls),
    # path('', include('about.urls')),
    path('blog/', include('blog.urls' ,namespace='blog')),
    path('property/', include('property.urls' ,namespace='property')),
    # path('accounts/', include('accounts.urls')),
    # path('settings/', include('settings.urls')),
]

# For media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
