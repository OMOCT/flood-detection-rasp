from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, FloodDataSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import FloodData
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class DataListView(generics.ListAPIView):
    serializer_class = FloodDataSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]

    def get_queryset(self):
        data = FloodData.objects.all().order_by('-timestamp')[:10]
        return data


# @api_view(["POST"])
# def receive_data(request):
#     serializer = FloodDataSerializer(data=request.data)
#
#     if serializer.is_valid():
#         serializer.save()
#         return Response({"message": "Data Saved"})
#
#     return Response(serializer.errors)

class FloodDataAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = FloodDataSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Data saved successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # def get(self, request):
    #     data = FloodData.objects.all().order_by('-timestamp')[:10]
    #     serializer = FloodDataSerializer(data, many=True)
    #     return Response(serializer.data)
