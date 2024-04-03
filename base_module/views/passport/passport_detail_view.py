from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ...serializers import PassportSerializer
from ...models import Passport


class PassportDetailView(RetrieveUpdateDestroyAPIView):
	"""
    Retrieve, update or delete a model instance.
    """
	queryset = Passport.objects.all()
	serializer_class = PassportSerializer
