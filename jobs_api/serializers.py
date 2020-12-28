from rest_framework import serializers
from .models import Jobs, User, Candidates,Work_record,questionnaire
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password':{'write_only':True, 'required':True}} # extract password and hide. System secure and protected!

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id','job','qualifications','experience','reporting_to')

class CandidatesSerializer(serializers.ModelSerializer):
    apply_for = serializers.StringRelatedField(many=True)
    work_record = serializers.StringRelatedField(many=True)
    class Meta:
        model = Candidates
        fields = ('id', 'name','work_record','apply_for')

class Work_recordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Work_record
        fields = ('id','positon','workplace','start','end')

class QuestionnaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = questionnaire
        fields = ('id', 'candidate', 'question', 'answer', 'mark')
