"""
URL configuration for sprint1 project.

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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from submitData import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from submitData.views import SubmitDetailData, SubmitData

router = routers.DefaultRouter()
# router.register(r'users', views.UsersViewSet)
# router.register(r'coordinates', views.CoordinatesViewSet)
# router.register(r'levels', views.LevelsViewSet)
router.register(r'pereval', views.PerevalViewSet)
# router.register(r'images', views.ImagesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api/submitData/', include(router.urls)),
    path('api/v2/submitData/<int:pk>/', SubmitDetailData.as_view(), name='submitDetailData'),
    path('api/v2/submitData/email/', SubmitData.as_view(), name='email'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
