from rest_framework import serializers
from .models import financial_records

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = financial_records
        fields = '__all__'
        read_only_fields = ['user']

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Amount must be positive")
        return value