from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('api/user', views.UserViewSets, basename='user-api')

urlpatterns = router.urls
