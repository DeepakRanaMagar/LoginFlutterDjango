from rest_framework import generics

from .models import Email
from .serializers import EmailSerializer

class EmailList(generics.ListAPIView):
    queryset = Email.objects.all()
    serializer_class = EmailSerializer
    
