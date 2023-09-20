from rest_framework import serializers
from .models import Users


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

    def validate(self, data):
        specialChar = '`~!@#$%^&*()-_=+{}[];:\'" ,./?'
        numeric = '1234567890'
        validSpecialChar = ['%', '@', '$', '"', '-', '_']
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'

        if any(i in specialChar for i in data["name"]):
            raise serializers.ValidationError("name is not contain Special Character")

        if not len(data['password']) >= 8:
            raise serializers.ValidationError('Password should be eight Char')

        if not any(i in upper_alphabet for i in data['password']):
            raise serializers.ValidationError("should be one upper case")

        if not any(i in lower_alphabet for i in data['password']):
            raise serializers.ValidationError('should be one lower case')

        if not any(i in numeric for i in data['password']):
            raise serializers.ValidationError('password at least one numeric')

        if not any(i in validSpecialChar for i in data['password']):
            raise serializers.ValidationError(f"({validSpecialChar})password should be contain special char")

        return data
