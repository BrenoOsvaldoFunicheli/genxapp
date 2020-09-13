from django.test import TestCase

from django.contrib.auth.models import User 
# Create your tests here.

class UserModelTest(TestCase):

    def setUp(self):
        user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

        # At this point, user is a User object that has already been saved
        # to the database. You can continue to change its attributes
        # if you want to change other fields.
        user.last_name = 'Lennon'
        user.save()

    def test_create_user(self):
        
        user_count = User.objects.all().count()

        self.assertEqual(user_count,1,"User doesn't created...")

    def test_to_error(self):
        self.assertEqual(1,1,"One doesn't is like the Two")

class UserEndpointTest(TestCase):

    def test_access_api(self):
        self.assertEqual(1,1,"The API can be access...")
