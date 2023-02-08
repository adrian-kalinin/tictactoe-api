from django.urls import include, path
from rest_framework.routers import DefaultRouter

from game import views

router = DefaultRouter()
router.register("games", views.GameViewSet)

app_name = "game"

urlpatterns = [path("", include(router.urls))]
