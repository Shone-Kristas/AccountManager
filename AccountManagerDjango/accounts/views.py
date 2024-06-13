from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UsersSerializer



class UsersAPIView(APIView):
    def post(self, request, format=None):
        headers = request.headers
        content_type = headers.get('x-Device')

        data = request.data

        print("Content-Type:", content_type)
        print("Data:", data)

        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






# @api_view(['POST'])
# def create_user(request):
#     device = request.headers.get('x-Device')
#
#     if not device:
#         return Response({"error": "x-Device header is required."}, status=status.HTTP_400_BAD_REQUEST)
#
#     data = request.data.copy()
#
#     if device == 'mail':
#         validate_mail(data)
#     elif device == 'mobile':
#         validate_mobile(data)
#     else:
#         return Response({"error": "Invalid x-Device header value."}, status=status.HTTP_400_BAD_REQUEST)
#
#     serializer = UserSerializer(data=data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateUserView(generics.CreateAPIView):
#     def get_serializer_class(self):
#         device = self.request.META.get('HTTP_X_DEVICE')
#
#         if device == 'mail':
#             return MailUserSerializer
#         elif device == 'mobile':
#             return MobileUserSerializer
#         elif device == 'web':
#             return WebUserSerializer
#         else:
#             return None
#
#     def create(self, request, *args, **kwargs):
#         serializer_class = self.get_serializer_class()
#         if serializer_class is None:
#             return Response({'error': 'Unsupported device'}, status=status.HTTP_400_BAD_REQUEST)
#
#         serializer = serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)