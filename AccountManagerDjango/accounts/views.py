from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from .serializers import mailSerializer, mobileSerializer, webSerializer
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