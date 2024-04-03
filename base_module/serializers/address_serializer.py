from rest_framework import serializers

from ..models import Address


# Serializers define the API representation.
class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields = '__all__'
