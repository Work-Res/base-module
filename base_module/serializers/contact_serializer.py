from rest_framework import serializers

from ..models import Contact


# Serializers define the API representation.
class ContactSerializer(serializers.ModelSerializer):
	class Meta:
		model = Contact
		fields = '__all__'
