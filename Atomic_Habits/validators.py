from django.core.exceptions import ValidationError
from datetime import timedelta


def validate_related_habit_and_reward(value):
    if value.relted_habbit and value.reward:
        raise ValidationError(
            "Нельзя одновременно выбрать связанную привычку и указание вознаграждения."
        )


def validate_execution_time(execution_time):
    max_execution_time = timedelta(seconds=120)
    execution_time_timedelta = timedelta(
        hours=execution_time.hour,
        minutes=execution_time.minute,
        seconds=execution_time.second
    )

    if execution_time_timedelta > max_execution_time:
        raise ValidationError("Время выполнения не может быть больше 120 секунд.")


def validate_related_habit(value):
    if value.relted_habbit and not value.relted_habbit.good_habit_sign:
        raise ValidationError(
            "В связанные привычки могут попадать только привычки с признаком приятной привычки."
        )


def validate_good_habit(habit):
    print("Inside validate_good_habit")  # Вывод отладочного сообщения
    print("habit.good_habit_sign:", habit.good_habit_sign)
    print("habit.reward:", habit.reward)
    print("habit.relted_habbit:", habit.relted_habbit)

    if habit.good_habit_sign:
        if habit.reward or habit.relted_habbit:
            raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")



def validate_periodicity(periodicity):
    min_periodicity_days = 7
    if periodicity > min_periodicity_days:
        raise ValidationError("Привычку нельзя выполнять реже, чем 1 раз в 7 дней.")
