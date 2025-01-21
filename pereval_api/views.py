from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PerevalSerializer
from .models import Pereval

class SubmitDataView(APIView):
    def post(self, request):
        serializer = PerevalSerializer(data=request.data)
        if serializer.is_valid():
            pereval = serializer.save()
            return Response({
                'status': status.HTTP_200_OK,
                'message': 'Отправлено успешно',
                'id': pereval.id
            }, status=200)
        return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'id': None
        }, status=400)