from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, UserAdsListView, CommentViewSet

router = SimpleRouter()
router.register('ads', AdViewSet, basename='ads')
router.register('ads/(?P<ad_pk>[^/.]+)/comments', CommentViewSet, basename='comments')

urlpatterns = [
    path('ads/me/', UserAdsListView.as_view(), name='user_ads'),
    path('', include(router.urls)),
]
