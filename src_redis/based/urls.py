from django.urls import path, include
from rest_framework import routers
from .views import ( SummarizeTextView,UserViewSet,UserProfileViewSet,DocumentViewSet,ProcessedDataViewSet,SubscriptionPlanViewSet,UserSubscriptionViewSet)

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('user-profiles', UserProfileViewSet)
router.register('documents', DocumentViewSet)
router.register('processed-data', ProcessedDataViewSet)
router.register('subscription-plans', SubscriptionPlanViewSet)
router.register('user-subscriptions', UserSubscriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/summarize/', SummarizeTextView.as_view(), name='summarize-text'),

]
