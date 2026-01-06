from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

import geetha
from geetha_app1 import serializer
from geetha_app1.models import User


# Create your views here.
# class GeethaAPIView(APIView):
#     permission_classes = (IsAuthenticated,)
#     def post(self,request):
#
#         geetha = Geetha()
#         geetha.name = request.data['name']
#         geetha.address = request.data['address']
#         geetha.city = request.data['city']
#         geetha.state = request.data['state']
#         geetha.save()
#         return Response({'status': 'data saved'})
#
#     def get(self,request):
#         Geet= Geetha.objects.all()
#         serializer = GeethaSerializer(Geet, many=True)
#         return Response(serializer.data)
#
#
#     def put(self, request):
#          geetha = Geetha.objects.all().values()
#          return Response(list(geetha))
#     def patch(self,request):
#         geetha = Geetha.objects.all().values()
#         return Response(list(geetha))
#     def delete(self,request):
#         geetha = Geetha.objects.all().values()
#         return Response(list(geetha))


class SignupView(APIView):
    permission_classes = (AllowAny,)
    def post(self, request):
        user = User()
        user.email = request.data['email']
        user.password = request.data['password']

        user.save()
        return Response({'email': user.email}, status=status.HTTP_201_CREATED)

# class signup(APIView):
#     permission_classes = (AllowAny,)
#     def post(self, request):
#         User = user()
#         user. adress = request.data['adress']
#         user.email = request.data['email']
#
#
#         user.save()
#         return Response({'adress': user.adress}, status=status )

















class userLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, user=None):
        username = request.data.get("username")
        password = request.data.get("password")

        if not username or not password:
            return Response({"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(name=username,password=password).first()

        if user is None:
            return Response({"error": "Invalid credentials "}, status=status.HTTP_401_UNAUTHORIZED)

        # Generate token
        refresh = RefreshToken.for_user(user)
        return Response({
            "username":user.name,
            "refresh": str(refresh),
            "access": str(refresh.access_token)
        })




