from rest_framework import serializers
from .models import employee


class employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = "__all__"


from django.contrib.auth.models import User
class register_serializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']