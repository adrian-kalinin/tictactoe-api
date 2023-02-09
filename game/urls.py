from rest_framework.routers import DefaultRouter

from game import views

app_name = "game"

router = DefaultRouter()
router.register("games", views.GameViewSet, basename="game")

urlpatterns = router.urls
