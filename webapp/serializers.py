from rest_framework import serializers  ## to convert our model to JSON format
from .models import employees

class employeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = employees
        # fields = ('firstname','lastname','emp_id')  #to display firstname and lastname in the format
        fields = '__all__'  # to display all fields

        def create(self, validated_data):
            return employees.objects.create(**validated_data)



