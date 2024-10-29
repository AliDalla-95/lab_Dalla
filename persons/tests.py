from django.test import TestCase
from .models import Person

# Create your tests here.

class PersonModelTest(TestCase):
    def setUp(self):
        Person.objects.create(name="ali dalla", age=30)
    
    def test_person_creation(self):
        person = Person.objects.get(name="ali dalla")
        self.assertEqual(person.age, 30)