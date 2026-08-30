from ..models import FoodEntry


class FoodEntryService:
    @staticmethod
    def save(**data):
        return FoodEntry.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for field, val in data.items():
            setattr(instance, field, val)
        instance.save()
        return instance

    @staticmethod
    def get_all():
        return FoodEntry.objects.all()

    @staticmethod
    def get_by_id(id):
        return FoodEntry.objects.get(pk=id)

    @staticmethod
    def delete(instance):
        instance.delete()
