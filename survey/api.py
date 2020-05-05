from rest_framework import viewsets, permissions, renderers
from rest_framework import filters
from rest_framework.parsers import MultiPartParser
from .models import Survey, SurveyResult
from .serializers import SurveySerializer, SurveyResultSerializer

class SurveyViewSet(viewsets.ModelViewSet):
    queryset= Survey.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SurveySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
    renderer_classes = [renderers.JSONRenderer]
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)

class SurveyResultViewSet(viewsets.ModelViewSet):
    queryset= SurveyResult.objects.all()
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = SurveyResultSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    
    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)
    