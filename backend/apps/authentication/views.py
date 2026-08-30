from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_403_FORBIDDEN,
)

from .serializers import (
    UserEditAdminSerializer,
    UserLoginSerializer,
    UserReturnSerializer,
    UserSerializer,
)
from .services.user_service import UserService

# Create your views here.


@api_view(["POST"])
@permission_classes([AllowAny])
def create_user_view(request):
    # If I do not pass a model to the serializer, it tries to create on save
    serializer = UserSerializer(data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)

    try:
        user = serializer.save()

        return Response(
            {
                "message": "User created successfully",
                "id": user.id,
            },
            status=HTTP_201_CREATED,
        )
    except Exception:
        return Response(
            {
                "message": "Could not create the user",
            },
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["POST"])
@permission_classes([AllowAny])
def login_view(request):
    serializer = UserLoginSerializer(data=request.data, partial=False)
    serializer.is_valid(raise_exception=True)

    user = UserService.login(request, serializer.validated_data)

    if user is not None:
        return Response(
            {
                "message": "User authenticated successfully",
                "id": user.id,
            },
            status=HTTP_200_OK,
        )
    else:
        return Response(
            {
                "message": "The account could not be accessed.",
            },
            status=HTTP_403_FORBIDDEN,
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def logout_view(request):
    UserService.logout(request)
    return Response(
        {
            "message": "successfully logged out",
        },
        status=HTTP_200_OK,
    )


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def all_view(request):
    users = UserService.get_all()
    return Response(UserReturnSerializer(users, many=True).data, status=HTTP_200_OK)


@api_view(["PATCH"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAdminUser])
def edit_user_admin_view(request, user_id):

    # If I do not pass a model to the serializer, it tries to update on save
    user = UserService.get_by_id(user_id)
    serializer = UserEditAdminSerializer(user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)

    try:
        serializer.save()
        return Response(UserReturnSerializer(serializer.data).data, status=HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "Could not update the user",
            },
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["PATCH"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def edit_user_view(request):
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)

    try:
        serializer.save()
        return Response(UserReturnSerializer(serializer.data).data, status=HTTP_200_OK)
    except Exception:
        return Response(
            {
                "message": "Could not update the user",
            },
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["PATCH"])
@permission_classes([AllowAny])
def change_password_view(request):
    serializer = UserLoginSerializer(data=request.data, partial=False)
    serializer.is_valid(raise_exception=True)

    try:
        UserService.change_password(serializer.validated_data)
        return Response(
            {
                "message": "successfully changed password",
            },
            status=HTTP_200_OK,
        )
    except Exception:
        return Response(
            {
                "message": "Could not change user's password",
            },
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["DELETE"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def delete_view(request):

    try:
        UserService.delete(request.user)
        return Response(
            {
                "message": "User deleted successfully",
            },
            status=HTTP_200_OK,
        )
    except Exception:
        return Response(
            {
                "message": "Coud not delete the user",
            },
            status=HTTP_400_BAD_REQUEST,
        )


@api_view(["GET"])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_logged_user_view(request):
    user = request.user

    return Response(UserReturnSerializer(user).data, status=HTTP_200_OK)
