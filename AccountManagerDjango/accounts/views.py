from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .models import User
from .serializers import mailSerializer, mobileSerializer, webSerializer, UserSerializer
from .validators import validate_mail, validate_mobile, validate_web


class UsersAPIView(APIView):
    def post(self, request, format=None):
        headers = request.headers
        content_type = headers.get('x-Device')

        if not content_type:
            return Response({"error": "x-Device header is required"}, status=status.HTTP_400_BAD_REQUEST)

        data = request.data

        try:
            if content_type == 'mail':
                validate_mail(data)
                serializer = mailSerializer(data=request.data)
            elif content_type == 'mobile':
                validate_mobile(data)
                serializer = mobileSerializer(data=request.data)
            elif content_type == 'web':
                validate_web(data)
                serializer = webSerializer(data=request.data)
            else:
                return Response({"error": "Unsupported x-Device type"}, status=status.HTTP_400_BAD_REQUEST)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except ValidationError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class UserDetailView(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)