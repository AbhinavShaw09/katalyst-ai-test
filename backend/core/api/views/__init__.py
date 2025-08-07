from rest_framework import viewsets
from rest_framework.response import Response
from .accounts import *

class HealthCheckViewSet(viewsets.ViewSet):
    authentication_classes = []
    permission_classes = []
    
    def list(self, request):
        return Response({"status": "ok"})