from rest_framework import serializers
from .models import Person, Detail

class DetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Detail
        fields = ['mobile_number', 'email', 'Address']
         
    
class PersonSerializers(serializers.ModelSerializer):
    details = DetailSerializers(many=True, read_only=True)
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'details']

 
    
