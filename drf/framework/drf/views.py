# from ast import Not
# from re import U
from urllib import response
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from.serializers import UserSerializer,TransformerSerializer,StudentSerializer
from.models import User,Transformer,Student
from rest_framework.generics import ListCreateAPIView
import datetime
import jwt
from rest_framework import status
from django.http import Http404
from django_filters.rest_framework import DjangoFilterBackend
 


# Create your views here.
class RegisterView(APIView):
    def post(self,request):
      serializer=UserSerializer(data=request.data)
      serializer.is_valid(raise_exception =True)
      serializer.save()
      return Response(serializer.data)

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password=request.data['password']
        user=User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('not a user')

        if not user.check_password(password):
            raise AuthenticationFailed('incorrect password')
        payload = {
            'id' : user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.utcnow()
        }
        token= jwt.encode(payload,'secret',algorithm='HS256')
        response =Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data=({
            'jwt':token
        })
        return response

class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed('unauthenticated')

        try:
            payload= jwt.decode(token,'secret',algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
               raise AuthenticationFailed('unauthenticated')
        
        user=User.objects.filter(id=payload['id']).first()
        serializer=UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('jwt')
        response.data ={
            'message':'success'
        }
        return response

# class TransformerList(APIView):
#     """
#     List all Transformers, or create a new Transformer
#     """
  
#     def get(self, request, format=None):
#         transformers = Transformer.objects.filter(text='sdggd')
#         serializer = TransformerSerializer(transformers, many=True)
#         return Response(serializer.data)
  
#     def post(self, request, format=None):
#         serializer = TransformerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class TransformerDetail(APIView):
#     """
#     Retrieve, update or delete a transformer instance
#     """
#     def get_object(self, pk):
#         # Returns an object instance that should 
#         # be used for detail views.
#         try:
#             return Transformer.objects.get(pk=pk)
#         except Transformer.DoesNotExist:
#             raise Http404
  
#     def get(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer)
#         return Response(serializer.data)
  
#     def put(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
#     def patch(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         serializer = TransformerSerializer(transformer,
#                                            data=request.data,
#                                            partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         transformer = self.get_object(pk)
#         transformer.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class student(ListCreateAPIView):
#     # queryset= Student.objects.filter(firstname="rinav")
#     queryset= Student.objects.all()
#     serializer_class= StudentSerializer
#     filter_backends=[DjangoFilterBackend]
#     filter_fieldset=['firstname','id','lastname','std','section']
#     # def get_queryset(self):
#     #     user=self.request.user
#     #     return Student.objects.filter(passby=user)