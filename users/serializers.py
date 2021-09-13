from rest_framework import serializers
from rest_api.models import User


# SHORT WAY

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'surname', 'telephone']


# LONG WAY

# class UserSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(required=True, max_length=32)
#     surname = serializers.CharField(required=True, max_length=32)
#     telephone = serializers.CharField(required=False, max_length=16)
#
#     def create(self, validated_data):
#         return User.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.id = validated_data.get('id', instance.id)
#         instance.name = validated_data.get('name', instance.name)
#         instance.surname = validated_data.get('surname', instance.surname)
#         instance.telephone = validated_data.get('telephone', instance.telephone)
#         instance.save()
#         return instance
#
