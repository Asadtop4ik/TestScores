from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import IELTS, Duolingo, TOEFL, CEFR
from .serializers import IELTS_Serializer, DuolingoSerializer, TOEFLSerializer, CEFRSerializer, TestScoresSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner


class IELTSViewSet(viewsets.ModelViewSet):
    queryset = IELTS.objects.all()
    serializer_class = IELTS_Serializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DuolingoViewSet(viewsets.ModelViewSet):
    queryset = Duolingo.objects.all()
    serializer_class = DuolingoSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TOEFLViewSet(viewsets.ModelViewSet):
    queryset = TOEFL.objects.all()
    serializer_class = TOEFLSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CEFRViewSet(viewsets.ModelViewSet):
    queryset = CEFR.objects.all()
    serializer_class = CEFRSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TestScoresListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        users_data = []

        ielts_scores = IELTS.objects.all()
        duolingo_scores = Duolingo.objects.all()
        toefl_scores = TOEFL.objects.all()
        cefr_scores = CEFR.objects.all()

        user_ids = set(
            list(ielts_scores.values_list('user_id', flat=True)) +
            list(duolingo_scores.values_list('user_id', flat=True)) +
            list(toefl_scores.values_list('user_id', flat=True)) +
            list(cefr_scores.values_list('user_id', flat=True))
        )

        for user_id in user_ids:
            data = {'user_id': user_id}

            try:
                ielts = IELTS.objects.get(user_id=user_id)
                data['ielts'] = IELTS_Serializer(ielts).data
            except IELTS.DoesNotExist:
                data['ielts'] = None

            try:
                duolingo = Duolingo.objects.get(user_id=user_id)
                data['duolingo'] = DuolingoSerializer(duolingo).data
            except Duolingo.DoesNotExist:
                data['duolingo'] = None

            try:
                toefl = TOEFL.objects.get(user_id=user_id)
                data['toefl'] = TOEFLSerializer(toefl).data
            except TOEFL.DoesNotExist:
                data['toefl'] = None

            try:
                cefr = CEFR.objects.get(user_id=user_id)
                data['cefr'] = CEFRSerializer(cefr).data
            except CEFR.DoesNotExist:
                data['cefr'] = None

            users_data.append(data)

        return Response(users_data, status=status.HTTP_200_OK)
