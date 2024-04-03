from rest_framework.generics import RetrieveUpdateDestroyAPIView

from ...models import Person
from ...serializers import PersonSerializer


class PersonDetailView(RetrieveUpdateDestroyAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

