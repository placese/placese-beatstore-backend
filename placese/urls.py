from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from beatstore.views import BeatViewSet

router = routers.DefaultRouter()
router.register(r'beats', BeatViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

urlpatterns += router.urls
