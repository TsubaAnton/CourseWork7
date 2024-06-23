from datetime import timedelta
from django.db import models
from config import settings
NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь', related_name='owner', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='Место')
    time = models.DateTimeField(auto_now_add=True, verbose_name='Время')
    action = models.CharField(max_length=100, verbose_name='Действие')
    is_pleasant = models.BooleanField(default=False, verbose_name='Признак приятной привычки')
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    period = models.PositiveIntegerField(default=1)
    reward = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)
    duration = models.DurationField(default=timedelta(minutes=2), verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
