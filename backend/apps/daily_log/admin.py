from django.contrib import admin

from apps.daily_log.models import DailyLog

# Register your models here.


@admin.register(DailyLog)
class DailyLogAdmin(admin.ModelAdmin):
    model = DailyLog
    list_display = ["user", "date"]
    search_fields = ["user"]
