from django.contrib import admin

from Atomic_Habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "user",
        "activity",
        "reward",
        "of_publicity",
        "time",
        "good_habit_sign",
        "periodicity",
        "execution_time",
    )  # отображение на дисплее
    list_filter = ("place", "user", "activity", "reward")  # фильтр
    search_fields = ("place", "user", "activity", "reward")  # поля поиска
