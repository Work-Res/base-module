from rest_framework.generics import ListCreateAPIView

from ...models import Address
from ...serializers import AddressSerializer


class AddressListCreateView(ListCreateAPIView):
	"""List or create model instance for Address"""
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	permission_classes = []

