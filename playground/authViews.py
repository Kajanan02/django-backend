from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from .serializers import UserSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.response import Response




def validateToken(token):
    if token and token.startswith('Bearer '):
        token_key = token.split(' ')[1]
        try:
            token_obj = Token.objects.get(key=token_key)
            user = token_obj.user
            return user
        except Token.DoesNotExist:
            return False
    else:
        return False

@api_view(['POST', 'PUT'])
@parser_classes([JSONParser])
def LoginApi(request):
    if request.method == 'POST':

        data = request.data
        provided_token = request.META.get('HTTP_AUTHORIZATION')

        if provided_token and provided_token.startswith('Bearer '):
            token_key = provided_token.split(' ')[1]

            try:
                token = Token.objects.get(key=token_key)
                user = token.user

                if user:
                    user_info = {
                        "is_superuser": user.is_superuser,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email
                    }

                    return JsonResponse({
                        "user": user_info,
                        "token": token.key,
                        "message": True,
                    }, status=status.HTTP_200_OK)


            except Token.DoesNotExist:
                return JsonResponse({
                    "message": "Invalid token"
                }, status=status.HTTP_401_UNAUTHORIZED)


        elif data:
            username = data.get('username')
            password = data.get('password')
            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)

                if created == False:
                    token.delete()
                    token = Token.objects.create(user=user)

                user_info = {
                    "is_superuser": user.is_superuser,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email
                }

                return JsonResponse({
                    "user": user_info,
                    "token": token.key,
                    "message": True,
                }, status=status.HTTP_200_OK)

            else:
                return JsonResponse({
                    'error': 'Invalid credentials or token',
                }, status=status.HTTP_401_UNAUTHORIZED)

        else:
            return JsonResponse({
                'error': 'Invalid credentials or token',
            }, status=status.HTTP_401_UNAUTHORIZED)

    elif request.method == 'PUT':
        provided_token = request.META.get('HTTP_AUTHORIZATION')
        isValidToken = validateToken(provided_token)

        if isValidToken:
            userId = isValidToken.id
            data = request.data
            if 'oldpassword' in request.data:
                oldpassword = request.data.get('oldpassword')
                newpassword = request.data.get('password')

                passs = {"password": newpassword}

                # Check if the provided old password matches the existing user password
                if isValidToken.check_password(oldpassword):
                    isValidToken.set_password(newpassword)
                    isValidToken.save()
                    return Response({"message": "Password updated successfully"}, status=status.HTTP_200_OK)


                else:
                    return Response({"error": "Incorrect old password"}, status=status.HTTP_400_BAD_REQUEST)

            else:
                try:
                    userInstance = UserSerializer(instance=isValidToken, data=data, partial=True)
                    if userInstance.is_valid():
                        userInstance.save()


                    else:
                        return Response({"Message": userInstance.errors}, status=status.HTTP_400_BAD_REQUEST)

                except isValidToken.DoesNotExist:
                        return Response({"message": "user not found"}, status=status.HTTP_404_NOT_FOUND)


        else:
            return Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

