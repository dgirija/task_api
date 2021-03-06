from .views import RegisterAPI, LoginAPI,ChangePasswordView
from knox import  views as knox_views
from django.urls import path, include
from rest_framework.routers import  DefaultRouter
from . import views

# Creating Router Object
router= DefaultRouter()

# Register ContactModelViewset with Router
router.register('contactapi', views.ContactModelViewSet, basename='contacts')

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls',namespace='rest_framework'))
]
