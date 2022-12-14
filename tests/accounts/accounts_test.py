from django.test import TestCase
from django.urls import reverse


class SignUpViewTests(TestCase):
    VALID_USER_DATA = {
        'username': 'test_user',
        'email': 'test_user@abv.bg',
        'password1': 'NAFyrYmLgh9zv2Y',
        'password2': 'NAFyrYmLgh9zv2Y',
    }

    def test_signup__when_valid_data__expect_log_in_user(self):
        response = self.client.post(
            reverse('register user'),
            data=self.VALID_USER_DATA,
        )

        self.assertEqual(self.VALID_USER_DATA['username'], response.context['user'].username)
