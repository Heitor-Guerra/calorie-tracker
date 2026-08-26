from django.contrib.auth import authenticate, login, logout

from ..models import User


class UserService:
    @staticmethod
    def save(data):
        return User.objects.create_user(**data)

    @staticmethod
    def update(instance, data):
        for field, val in data.items():
            setattr(instance, field, val)
        instance.save()
        return instance

    @staticmethod
    def login(request, data):
        email = data["email"]
        password = data["password"]
        user = authenticate(request=request, email=email, password=password)

        if user is not None:
            login(request, user)

        if not user.is_active:
            raise Exception("User is not active")

        return user

    @staticmethod
    def logout(request):
        logout(request)

    @staticmethod
    def get_all():
        return User.objects.all()

    @staticmethod
    def get_by_id(id):
        return User.objects.get(pk=id)

    @staticmethod
    def delete(instance):
        instance.delete()
