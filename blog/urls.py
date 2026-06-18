from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]



router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns += [
    path('api/', include(router.urls)),
]
