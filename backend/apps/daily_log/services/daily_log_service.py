from apps.authentication.services.user_service import UserService
from apps.daily_log.models import DailyLog


class DailyLogService:
    @staticmethod
    def save(data):
        user_id = data.pop("user_id", None)
        if user_id is not None:
            user = UserService.get_by_id(user_id)

        log = DailyLog.objects.create(user=user, **data)

        return log

    @staticmethod
    def get_all():
        return DailyLog.objects.all()

    @staticmethod
    def get_by_id(id):
        return DailyLog.objects.get(pk=id)

    @staticmethod
    def get_all_by_user_id(user_id):
        return DailyLog.objects.filter(user__id=user_id)

    @staticmethod
    def delete(instance):
        instance.delete()
