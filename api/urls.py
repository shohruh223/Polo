from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import CategoryAPIView, ProductAPIView

router = DefaultRouter()
router.register('product', ProductAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('category/', CategoryAPIView.as_view())
]