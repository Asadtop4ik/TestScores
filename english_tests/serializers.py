from rest_framework import serializers
from .models import IELTS, Duolingo, TOEFL, CEFR


class IELTS_Serializer(serializers.ModelSerializer):
    class Meta:
        model = IELTS
        fields = '__all__'


class DuolingoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Duolingo
        fields = '__all__'


class TOEFLSerializer(serializers.ModelSerializer):
    class Meta:
        model = TOEFL
        fields = '__all__'


class CEFRSerializer(serializers.ModelSerializer):
    class Meta:
        model = CEFR
        fields = '__all__'


class TestScoresSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    ielts = IELTS_Serializer(required=False, allow_null=True)
    duolingo = DuolingoSerializer(required=False, allow_null=True)
    toefl = TOEFLSerializer(required=False, allow_null=True)
    cefr = CEFRSerializer(required=False, allow_null=True)

