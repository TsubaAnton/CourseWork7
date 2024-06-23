from rest_framework import serializers
from .models import Habit
from .validators import ChoiceValidator, TimeExecutionValidator, PleasantValidator, PleasantOrRewardValidator, PeriodicityValidator


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = '__all__'
        validators = [ChoiceValidator(field1='related_habit', field2='reward'),
                      TimeExecutionValidator(field='duration'),
                      PleasantValidator(field1='related_habit', field2='is_pleasant'),
                      PleasantOrRewardValidator(field1='reward', field2='related_habit'),
                      PeriodicityValidator(field='period')]
