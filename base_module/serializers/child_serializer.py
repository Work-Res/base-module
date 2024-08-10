from rest_framework import serializers
from ..models import Child


class ChildSerializer(serializers.ModelSerializer):

    class Meta:
        model = Child
        fields = (
            "first_name",
            "last_name",
            "age",
            "gender",
            "is_applying_residence",
        )
