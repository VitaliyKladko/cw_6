from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet, basename='ads')

# TODO настройка роутов для модели
urlpatterns = [
    path('', include(ads_router.urls))
]
