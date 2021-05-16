from rest_framework import routers
from .apis import CategoryViewSet


router = routers.SimpleRouter()
router.register('api/categories', CategoryViewSet,'categories')
urlpatterns = router.urls