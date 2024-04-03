from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse


class AddressListCreateTestCase(APITestCase):
	def setUp(self):
		self.url = reverse('address_list')
	
	def test_list_addresses(self):
		response = self.client.get(self.url)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(response.data), 0)
	
	def test_create_address(self):
		sample_address = {
			'street': '123',
			'country': 'Botswana',
			'town': 'Molepolole',
			'plot_no': '19611',
			'box_no': 'Box 2013',
			'post_office_location': 'Molepolole'
		}
		response = self.client.post(self.url, sample_address, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
	
	def test_create_invalid_address(self):
		sample_address = {
			'street': '123',
			'country': 'Botswana',
			'town': 'Molepolole',
			'plot_no': '19611',
			'box_no': 'Box 2013',
			'post_office_location': ''
		}
		response = self.client.post(self.url, sample_address, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		

