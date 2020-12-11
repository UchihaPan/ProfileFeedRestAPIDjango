from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileView, UserLoginApiView

router = DefaultRouter()
router.register('', UserProfileView)

urlpatterns = [
    path('api/', include(router.urls)),
    path('login/', UserLoginApiView.as_view()),

]
