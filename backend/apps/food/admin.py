from django.contrib import admin

from apps.food.models import Food
from apps.food.services.food_entry_service import FoodEntry

# Register your models here.


@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    model = Food
    list_display = ["name", "calories_per_100g"]
    search_fields = ["name"]


@admin.register(FoodEntry)
class FoodEntryAdmin(admin.ModelAdmin):
    model = FoodEntry
    list_display = ["food", "daily_log", "quantity_g"]
    search_fields = ["food"]
