from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()
    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'phone_number', 'user_name')

    def get_user_name(self, custObj):
        return custObj.user.name
    
    def validate(self, data):
        unexpected_fields = set(data.keys()) - set(self.fields)
        
        if unexpected_fields:
            raise serializers.ValidationError(f"Unexpected fields: {', '.join(unexpected_fields)}")
        
        return data