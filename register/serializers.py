from rest_framework import serializers

from register.models import CustomerUser


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = (
            'username',
            'full_name',
            'email',
            'password',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number'
        )

class VerifySerializer(serializers.ModelSerializer):

    token = serializers.CharField(max_length=555)
    class Meta:
        model = CustomerUser
        fields = ['token']
class UserLoginSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(max_length=255)
    class Meta:
        model = CustomerUser
        fields = [
            'email',
            'password'
        ]

class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'email',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]

class ChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = ['password']

class EditProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerUser
        fields = [
            'full_name',
            'country',
            'company_name',
            'user_type',
            'phone_number',
            'corporate_number',
        ]


    def update(self, instance, validated_data):

        instance.full_name = validated_data.get('full_name', instance.full_name)
        instance.country = validated_data.get('country', instance.country)
        instance.company = validated_data.get('company_name', instance.company_name)
        instance.user_type = validated_data.get('user_type', instance.user_type)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.corporate_number = validated_data.get('corporate_number', instance.corporate_number)
        instance.save()
        return instance