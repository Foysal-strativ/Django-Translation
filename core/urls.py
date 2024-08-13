from rest_framework.routers import DefaultRouter
from .views import PostView, TranslationView
from django.urls import path, include

router = DefaultRouter()

router.register('posts', PostView, basename='post')
urlpatterns = [
    path('', include(router.urls)),
    path("test/", TranslationView.as_view(), name="test"),
]