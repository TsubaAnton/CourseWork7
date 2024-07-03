from rest_framework.test import APITestCase
from users.models import User
from .models import Habit
from django.urls import reverse
from rest_framework import status


class HabitTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(
            email='test_email@test.com',
            password='1234',
        )
        self.habit = Habit.objects.create(
            user=self.user,
            place='Парк',
            time='18:00:00',
            action='Погулять',
            is_pleasant=False,
            related_habit=None,
            period=1,
            reward='Поесть мороженное',
            duration=120,
            is_public=True
        )
        self.habit2 = Habit.objects.create(
            user=self.user,
            place='Зал',
            time='18:00:00',
            action='Тренировка',
            is_pleasant=False,
            related_habit=None,
            period=2,
            reward='Поесть мороженное',
            duration=120,
            is_public=True
        )

    def test_habit_list(self):
        response = self.client.get(reverse('habits:habit_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_create(self):
        data = {'user': self.user.id, 'place': 'test_place', 'time': '12:00:00', 'action': 'test_action',
                'is_pleasant': False, 'related_habit': '', 'period': 2, 'reward': 'test_reward', 'duration': 60,
                'is_public': True
                }
        response = self.client.post(reverse('habits:habit_create'), data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_retrieve(self):
        response = self.client.get(reverse('habits:habit_retrieve', kwargs={'pk': self.habit.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        data = {'user': self.user.id, 'place': 'test_place', 'time': '12:00:00', 'action': 'test_action',
                'is_pleasant': False, 'related_habit': '', 'period': 2, 'reward': 'test_reward', 'duration': 60,
                'is_public': True
                }
        response = self.client.patch(reverse('habits:habit_update', kwargs={'pk': self.habit.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_destroy(self):
        response = self.client.delete(reverse('habits:habit_destroy', kwargs={'pk': self.habit.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
