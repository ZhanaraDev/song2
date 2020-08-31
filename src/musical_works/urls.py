from django.urls import path, include
from rest_framework import routers

from musical_works.views import MusicalWorksViewSet

router = routers.DefaultRouter()
router.register(r'musical_works', MusicalWorksViewSet)

urlpatterns = router.urls
