from django.db import transaction
from rest_framework import serializers

from apps.authentication.serializers import UserReturnSerializer
from apps.daily_log.services.daily_log_service import DailyLogService
from apps.food.serializers import FoodEntrySerializer
from apps.food.services.food_entry_service import FoodEntryService
from apps.food.services.food_service import FoodService


class DailyLogReturnSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    user = UserReturnSerializer(read_only=True)
    date = serializers.DateTimeField(read_only=True)
    entries = FoodEntrySerializer(many=True, read_only=True)


class DailyLogSerializer(serializers.Serializer):
    entries = FoodEntrySerializer(many=True, partial=True)

    @transaction.atomic
    def create(self, validated_data):
        entries = validated_data.pop("entries", [])
        log = DailyLogService.save(validated_data)

        for entry_data in entries:
            food_item = FoodService.get_by_name(entry_data["food"]["name"])
            if food_item is None:
                raise serializers.ValidationError("Food does not exist.")

            FoodEntryService.save(
                food=food_item,
                quantity_g=entry_data["quantity_g"],
                daily_log=log,
            )

        return log
