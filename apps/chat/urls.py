"""
urls used for chat app
"""
from django.urls import path, include

from apps.chat.views import QuestionViewSet
from apps.common.routers import OptionalSlashRouter

router = OptionalSlashRouter()
router.register(r'question', QuestionViewSet, basename='question')

urlpatterns = [
    path(r'chat/', include(router.urls)),
]