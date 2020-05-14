from rest_framework import generics
from django.db.models import Max
from rest_framework.response import Response
from .models import Report
from .serializers import ReportSerializer

class ReportView(generics.RetrieveAPIView):
    queryset = Report.objects.all().aggregate(Max('id'))
    serializer_class = ReportSerializer
