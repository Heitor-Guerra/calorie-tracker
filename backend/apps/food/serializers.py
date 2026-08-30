from rest_framework import serializers

from .services.food_service import FoodService


class FoodSerializer(serializers.Serializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()
    calories_per_100g = serializers.FloatField(read_only=True)

    def create(self, validated_data):
        return FoodService.save(validated_data)


class FoodsSerializer(serializers.Serializer):
    foods = FoodSerializer(many=True)

    def create(self, validated_data):
        foods_data = validated_data["foods"]

        return [FoodService.save(food_data) for food_data in foods_data]


class FoodEntrySerializer(serializers.Serializer):
    food = FoodSerializer()
    quantity_g = serializers.FloatField(min_value=0)
