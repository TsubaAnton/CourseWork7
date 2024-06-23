from rest_framework.serializers import ValidationError
from datetime import timedelta


class ChoiceValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('related_habit') and habit.get('reward'):
            raise ValidationError('Нельзя одновременно заполнять поле вознаграждения и связанной привычки')


class TimeExecutionValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('duration') > timedelta(minutes=2):
            raise ValidationError('Время выполнения должно быть не больше 120 секунд')


class PleasantValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('related_habit'):
            if not habit.get('is_pleasant'):
                raise ValidationError('В связанные привычки могут попадать только привычки с признаком приятной привычки')


class PleasantOrRewardValidator:
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, habit):
        if habit.get('reward') or habit.get('related_habit'):
            raise ValidationError('У приятной привычки не может быть вознаграждения или связанной привычки')


class PeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, habit):
        if habit.get('period') < 1 or habit.get('period') > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней')


