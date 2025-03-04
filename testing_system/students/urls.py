from django.urls import path, include
from .views import StudentViewSet, TestViewSet, TestResultViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'students', StudentViewSet)
router.register(r'tests', TestViewSet)
router.register(r'results', TestResultViewSet)
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]
