from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ads.apps import SalesConfig
from ads.views import AdViewSet, CommentViewSet


app_name = SalesConfig.name

router = DefaultRouter()
router.register(r'ads', AdViewSet, basename='ads')
router.register(r'ads/(?P<ad_pk>\d+)/comments', CommentViewSet, basename='comment')

urlpatterns = [path("", include(router.urls))]