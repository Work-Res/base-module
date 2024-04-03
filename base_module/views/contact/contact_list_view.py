from rest_framework.generics import ListCreateAPIView

from ...serializers import ContactSerializer
from ...models import Contact


class ContactListView(ListCreateAPIView):
	"""
    List or create a model instance.
    """
	queryset = Contact.objects.all()
	serializer_class = ContactSerializer
