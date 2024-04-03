from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class PersonListCreateTestCase(APITestCase):
	def setUp(self):
		self.url = reverse('person_list')
	
	def test_list_personal_details(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 0)
	
	def test_create_personal_details(self):
		sample_address = {
			'first_name': 'Test',
			'last_name': 'Test2',
			'middle_name': 'Test3',
			'maiden_name': 'Test4',
			'marital_status': 'single',
			'dob': '2022-01-20',
			'country_birth': 'Botswana',
			'place_birth': 'Molepolole',
			'gender': 'male',
			'occupation': 'Software Engineer',
			'qualification': 'Bachelor Degree in Computer Science'
		}
		response = self.client.post(self.url, sample_address, format='json')
		print(response.data)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	
	def test_create_invalid_personal_details(self):
		sample_address = {
			'first_name': '',
			'last_name': 'Test2',
			'middle_name': 'Test3',
			'maiden_name': 'Test4',
			'marital_status': 'Single',
			'dob': '20/01/2022',
			'country_birth': 'Botswana',
			'place_birth': 'Molepolole',
			'gender': 'Male',
			'occupation': 'Software Engineer',
			'qualification': 'Bachelor Degree in Computer Science'
		}
		response = self.client.post(self.url, sample_address, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


