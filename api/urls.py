"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import CategoryViewSet, EpisodesViewSet, FinalistViewSet, ServicesViewSet, PostViewSet
from django.conf.urls.static import static 
from django.conf import settings
from rest_framework_swagger.views import get_swagger_view
from core.views import vote
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'categorys', CategoryViewSet)
router.register(r'episodes', EpisodesViewSet)
router.register(r'finalists', FinalistViewSet)
router.register(r'services', ServicesViewSet)
router.register(r'post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('votar/', vote, name='votar')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)