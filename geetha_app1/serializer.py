# from rest_framework import serializers
# from .models import
#
# class GeethaSerializer(serializers.ModelSerializer):
#     name = serializers.CharField(max_length=100)
#     address = serializers.CharField(max_length=100)
#     city = serializers.CharField(max_length=100)
#     state = serializers.CharField(max_length=100)
#
#     class Meta:
#         model =
#         fields = [
#             'id',
#             'name',
#             'address',
#             'city',
#             'state'
#         from rest_framework import serializers
# from .models import User

from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']



