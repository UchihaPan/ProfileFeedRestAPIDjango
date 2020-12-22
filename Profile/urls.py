from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, UserLoginApiView,ProfileFeedView

router = DefaultRouter()
router.register('profile', UserProfileView)
router.register('feed', ProfileFeedView)


urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),

]
