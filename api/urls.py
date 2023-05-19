from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('to/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('to/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.api),
    path('users/', views.getUsers),
    path('users/<str:pk>', views.getUser),
]
