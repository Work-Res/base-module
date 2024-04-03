from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ...serializers import ContactSerializer
from ...models import Contact


class ContactDetailView(RetrieveUpdateDestroyAPIView):
	"""
    Retrieve, update or delete a model instance.
    """
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
