from rest_framework import serializers
from mac.models import emp

class empSerializer(serializers.ModelSerializer):
    class Meta:
        model=emp
        fields='__all__'