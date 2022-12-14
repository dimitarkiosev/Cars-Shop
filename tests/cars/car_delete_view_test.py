from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from tests.accounts.BaseTestCase import TestCaseBase
from tests.utils.creation_utils import create_car_for_user

UserModel = get_user_model()


class CarDeleteViewTests(TestCaseBase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@abv.bg',
        'password': 'NAFyrYmLgh9zv2Y',
    }

    def delete_car__when_owner__expect_owner_is_true(self):
        user = self._create_user_and_login(self.VALID_USER_DATA)
        car = create_car_for_user(user, count=1)

        response = self.client.get(reverse_lazy('delete car', kwargs={'pk': car.pk}))

        self.assertTrue(response.context['owner'])

