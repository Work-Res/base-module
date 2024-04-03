from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ...serializers import AddressSerializer
from ...models import Address


class AddressDetailView(RetrieveUpdateDestroyAPIView):
	"""
    Retrieve, update or delete a model instance.
    """
	queryset = Address.objects.all()
	serializer_class = AddressSerializer
	permission_classes = []
