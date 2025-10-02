from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RiderRegisterSerializer, DriverRegisterSerializer


class RiderRegisterView(APIView):
    def post(self, request):
        serializer = RiderRegisterSerializer(data=request.data)
        if serializer.is_valid():
            rider = serializer.save()
            return Response({"message": "Rider registered successfully", "rider": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DriverRegisterView(APIView):
    def post(self, request):
        serializer = DriverRegisterSerializer(data=request.data)
        if serializer.is_valid():
            driver = serializer.save()
            return Response({"message": "Driver registered successfully", "driver": serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
