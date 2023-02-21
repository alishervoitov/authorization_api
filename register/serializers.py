from rest_framework import serializers

from register.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = "__all__"