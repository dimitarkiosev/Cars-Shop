from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_car_for_user

UserModel = get_user_model()


class UserDetailsViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@abv.bg',
        'password': 'NAFyrYmLgh9zv2Y',
    }

    def test_user_details__when_owner__expect_is_owner_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertTrue(response.context['is_owner'])

    def test_user_details__when_not_owner__expect_is_owner_false(self):
        user2 = self._create_user_and_login({
            'username': self.VALID_USER_DATA['username'] + '1',
            'email': self.VALID_USER_DATA['email'] + '1',
            'password': self.VALID_USER_DATA['password'],
        })

        self._create_user_and_login(self.VALID_USER_DATA)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user2.pk}))

        self.assertFalse(response.context['is_owner'])

    def test_user_details__when_no_car__expect_empty_cars_count(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0,response.context['cars_count'])

    def test_user_details__when_no_car__expect_empty_total_value(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(0,response.context['total_value'])

    def test_user_details__when_car__expect_car(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_car_for_user(user, count=1)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(1, response.context['cars_count'])
        self.assertEqual(10000, response.context['total_value'])

    def test_user_details__when_5_cars__expect_5cars_value(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)

        create_car_for_user(user, count=5)

        response = self.client.get(reverse_lazy('details user', kwargs={'pk': user.pk}))

        self.assertEqual(5, response.context['cars_count'])
        self.assertEqual(50000, response.context['total_value'])


