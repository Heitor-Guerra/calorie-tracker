import logging

logger = logging.getLogger(__name__)

from django.utils import timezone
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.decorators import (
    APIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
)

from apps.daily_log.serializers import DailyLogReturnSerializer, DailyLogSerializer
from apps.daily_log.services.daily_log_service import DailyLogService

# Create your views here.


class DailyLogCRUDView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logs_by_user = DailyLogService.get_all_by_user_id(request.user.id)
        return Response(
            DailyLogReturnSerializer(logs_by_user, many=True).data, status=HTTP_200_OK
        )

    def post(self, request):
        serializer = DailyLogSerializer(data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            log = serializer.save(
                user_id=request.user.id,
                date=timezone.now(),
            )
            return Response(
                {"message": "Log saved Successfully", "id": log.id},
                status=HTTP_201_CREATED,
            )
        except Exception:
            return Response(
                {"message": "Could not save the log"}, status=HTTP_400_BAD_REQUEST
            )

    def delete(self, request):
        log = DailyLogService.get_by_id(request.data["id"])
        if log.user is not request.user:
            return Response(
                {
                    "message": "The user is not the owner of log",
                },
                status=HTTP_401_UNAUTHORIZED,
            )

        try:
            DailyLogService.delete(log)
            return Response(
                {
                    "message": "Log deleted successfully",
                },
                status=HTTP_200_OK,
            )
        except Exception:
            return Response(
                {
                    "message": "Could not delete the Log",
                },
                status=HTTP_400_BAD_REQUEST,
            )
