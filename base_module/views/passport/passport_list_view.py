from rest_framework.generics import ListCreateAPIView

from ...models import Passport
from ...serializers import PassportSerializer


class PassportListView(ListCreateAPIView):
	queryset = Passport.objects.all()
	serializer_class = PassportSerializer

