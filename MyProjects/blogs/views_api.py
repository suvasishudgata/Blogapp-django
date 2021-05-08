from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

class LoginView(APIView):

    def post(self, request):

        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'Username Not Found'
                raise Exception('Username Not Found')
            
            if data.get('password') is None:
                response['message'] = 'Password Not Found'
                raise Exception('Password Not Found')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'Username Not Found'
                raise Exception('Invalid Username')

            user_obj = authenticate(username=data.get('username'), password=data.get('password'))

            if user_obj:
                response['status'] = 200
                response['message'] = 'WELCOME!!'

            else:
                response['message'] = 'Invalid Password'
                raise Exception('Invalid Password')

        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()


class RegisterView(APIView):

     def post(self, request):
    
        response = {}
        response['status'] = 500
        response['message'] = 'Something Went Wrong'
        try:
            data = request.data
            if data.get('username') is None:
                response['message'] = 'Username Not Found'
                raise Exception('Username Not Found')
            
            if data.get('password') is None:
                response['message'] = 'Password Not Found'
                raise Exception('Password Not Found')
            
            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'Username Already Taken'
                raise Exception('Username Already Taken')
            
            user_obj = User.objects.create(username=data.get('username'))
            user_obj.set_password(data.get('password'))
            user_obj.save()
            response['status'] = 200
            response['message'] = 'Account Created!!'

        except Exception as e:
            print(e)

        return Response(response)

RegisterView = RegisterView.as_view()
