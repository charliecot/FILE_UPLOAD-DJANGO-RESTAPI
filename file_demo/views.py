from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import CVUploadSerializer
from django.contrib.auth import get_user_model
from rest_framework.parsers import MultiPartParser,FormParser



# Create your views here.
def index(request):
    context={}
    return render(request,'index.html',context)









User = get_user_model()

class UploadCVView(APIView):
    serializer_class = CVUploadSerializer
    parser_classes = [MultiPartParser,FormParser]

    def post(self, request):
    
        user = User.objects.first()
        serializer = self.serializer_class(instance=user, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
