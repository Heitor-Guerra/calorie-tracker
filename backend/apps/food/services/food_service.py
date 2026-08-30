from ..models import Food


class FoodService:
    @staticmethod
    def save(data):
        return Food.objects.create(**data)

    @staticmethod
    def update(instance, data):
        for field, val in data.items():
            setattr(instance, field, val)
        instance.save()
        return instance

    @staticmethod
    def get_all():
        return Food.objects.all()

    @staticmethod
    def get_by_id(id):
        return Food.objects.get(pk=id)

    @staticmethod
    def get_by_name(name):
        return Food.objects.get(name=name)

    @staticmethod
    def delete(instance):
        instance.delete()
