from django.test import TestCase
from shop.models import Contact


class TestContact(TestCase):
    def setUp(self):
        self.data1 = {
            'first_name' : 'Qalib',
            'last_name' : 'Azizov',
            'email' : 'azizovgalib@mail.ru',
            'adress' : 'Huseyn Djavid',
            'phone' : '0556028525',
        }
        self.data2 = {
            'first_name' : 'Qalib2',
            'last_name' : 'Azizov2',
            'email' : 'azizovgalib2@mail.ru',
            'adress' : 'Huseyn Djavid',
            'phone' : '0556028525',
        }
        self.contact1 = Contact.objects.create(**self.data1)
        self.contact2 = Contact.objects.create(**self.data2)


    def test_model_data(self):
        self.assertEqual(self.data1['first_name'], self.contact1.first_name)
        self.assertEqual(self.data1['last_name'], self.contact1.last_name)
        self.assertEqual(self.data1['first_name'], self.contact1.first_name)
        self.assertEqual(self.data1['email'], self.contact1.email)
        self.assertEqual(self.data1['adress'], self.contact1.adress)
        self.assertEqual(self.data1['phone'], self.contact1.phone)


    def test_str_method(self):
        self.assertEqual(str(self.contact1), self.data1['first_name'])


    def tearDown(self):
        del self.contact1
        del self.contact2
        