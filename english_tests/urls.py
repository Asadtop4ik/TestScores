from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IELTSViewSet, DuolingoViewSet, TOEFLViewSet, CEFRViewSet, TestScoresListView

router = DefaultRouter()

router.register('ielts', IELTSViewSet)
router.register('duolingo', DuolingoViewSet)
router.register('toefl', TOEFLViewSet)
router.register('cefr', CEFRViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('test-scores/', TestScoresListView.as_view(), name='test-scores-list'),
]

