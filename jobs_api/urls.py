from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from .views import UserViewSet, JobsViewSet, CandidatesViewSet,Work_recordViewSet,QuestionnaireViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('Jobs', JobsViewSet)
router.register('Candidates', CandidatesViewSet)
router.register('Work_record', Work_recordViewSet)
router.register('Questionnaire', QuestionnaireViewSet)

urlpatterns = [
    path('',include(router.urls))
]
