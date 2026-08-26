from rest_framework import serializers

from .services.user_service import UserService


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    username = serializers.CharField()
    full_name = serializers.CharField()

    def create(self, validated_data):
        return UserService.save(validated_data)

    def update(self, instance, validated_data):
        return UserService.update(instance, validated_data)


class UserReturnSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(read_only=True)
    username = serializers.CharField(read_only=True)
    full_name = serializers.CharField(read_only=True)


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


class UserEditAdminSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()
    full_name = serializers.CharField()
    password = serializers.CharField()
    is_active = serializers.BooleanField()
    is_staff = serializers.BooleanField()
    is_superuser = serializers.BooleanField()

    def update(self, instance, validated_data):
        return UserService.update(instance, validated_data)
