from rest_framework.generics import ListCreateAPIView

from ...models import Person
from ...serializers import PersonSerializer


class PersonListView(ListCreateAPIView):
	queryset = Person.objects.all()
	serializer_class = PersonSerializer

