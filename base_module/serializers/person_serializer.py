from rest_framework import serializers

from ..models import Person


# Serializers define the API representation.
class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = '__all__'
