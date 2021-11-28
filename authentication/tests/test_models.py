from rest_framework.test import APITestCase
from authentication.models import User


class TestModel(APITestCase):
    def test_creates_user(self):
        user = User.objects.create_user('brian', 'gbrian@gmail.com', 'Pwd123!')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'gbrian@gmail.com')
        self.assertFalse(user.is_staff)

    def test_creates_superuser(self):
        user = User.objects.create_superuser(
            'brian', 'gbrian@gmail.com', 'Pwd123!')
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, 'gbrian@gmail.com')
        self.assertTrue(user.is_staff)

    def test_raises_value_error_when_no_username(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(
                username=None, email='gbrian@gmail.com', password='Pwd123!')
        # self.assertRaises(ValueError, User.objects.create_user,
        #                   username=None, email='gbrian@gmail.com', password='Pwd123!')

    def test_raises_value_error_when_no_is_staff_is_false_on_create_superuser(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username=None, email='gbrian@gmail.com', password='Pwd123!', is_staff=False)

    def test_raises_value_error_when_no_is_superuser_is_false_on_create_superuser(self):
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username=None, email='gbrian@gmail.com', password='Pwd123!', is_superuser=False)
