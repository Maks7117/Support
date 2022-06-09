
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/base-auth', include('rest_framework.urls')),
    path('api/v1/auth', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/support/', include('support.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),


]
