from django.urls import path

from Atomic_Habits.apps import AtomicHabitsConfig
from Atomic_Habits.views import (
    HabitCreateAPIView,
    HabitDestroyAPIView,
    HabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
)

app_name = AtomicHabitsConfig.name


urlpatterns = [
    path("habit/", HabitListAPIView.as_view(), name="habit-list"),
    path("habit/create/", HabitCreateAPIView.as_view(), name="habit-create"),
    path("habit/detail/<int:pk>/", HabitRetrieveAPIView.as_view(), name="habit-detail"),
    path("habit/delete/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit-delete"),
    path("habit/update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit-update"),
]
