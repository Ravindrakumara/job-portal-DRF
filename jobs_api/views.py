
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication #      with out "anonymous" erro pass
from .models import Jobs, User,Work_record,Candidates,questionnaire
from .serializers import UserSerializer, JobsSerializer, CandidatesSerializer, Work_recordSerializer,QuestionnaireSerializer #  Import serializers.py from serializers


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer



class Work_recordViewSet(viewsets.ModelViewSet):
    queryset = Work_record.objects.all()
    serializer_class = Work_recordSerializer

class CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Candidates.objects.all()
    serializer_class = CandidatesSerializer

class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer
    authentication_classes = (TokenAuthentication,)

