from django.contrib import admin
from django.urls import path, include 

from rest_framework.routers import SimpleRouter

from apps.info.api.views import TodoViewSet

router = SimpleRouter()
router.register("todos", TodoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
]