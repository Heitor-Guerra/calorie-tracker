from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)

from .serializers import FoodSerializer, FoodsSerializer
from .services.food_service import FoodService

# Create your views here.


@api_view(["POST"])
@permission_classes([IsAdminUser])
def create_food_view(request):
    serializers = FoodsSerializer(data=request.data)
    serializers.is_valid(raise_exception=True)

    try:
        serializers.save()
        return Response(
            {"message": "Items created successfully"}, status=HTTP_201_CREATED
        )
    except Exception:
        return Response(
            {"message": "Could not create Items"}, status=HTTP_400_BAD_REQUEST
        )


@api_view(["GET"])
@permission_classes([AllowAny])
def all_view(request):
    return Response(
        FoodSerializer(FoodService.get_all(), many=True).data, status=HTTP_200_OK
    )
