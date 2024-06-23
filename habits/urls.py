from .apps import HabitsConfig
from django.urls import path
from .views import HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, HabitUpdateAPIView, HabitDestroyAPIView, PublicHabitListAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/public/', PublicHabitListAPIView.as_view(), name='habit_list_public'),
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_retrieve'),
    path('habit/update/<int:pk>', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>', HabitDestroyAPIView.as_view(), name='habit_destroy'),
]
