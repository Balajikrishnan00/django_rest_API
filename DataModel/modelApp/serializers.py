from rest_framework import serializers
from modelApp.models import Person, Color, Students, Employee
from django.contrib.auth.models import User


# -------------------------------------------------------------
class LoginSerializers(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data


# ----------------------------------------------------------
class ColorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['color_name', 'id']


# -----------------------------------------------------------
class PersonSerializers(serializers.ModelSerializer):
    color = ColorSerializers()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Person
        fields = "__all__"
        # depth = True

    def get_country(self, data):
        color_obj = Color.objects.get(id=data.color.id)
        return {"color_name": color_obj.color_name, "hex": "#90"}


# --------------------------------------------------------
class StudentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


# --------------------------------------------------------
class EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


# -------------------------------------------------------
class RegisterSerializers(serializers.Serializer):
    username = serializers.CharField(max_length=30)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=50)

    def validate(self, data):

        specialChar = '`~!@#$%^&*()-_=+{}[];:\'" ,./?'
        numeric = '1234567890'
        validSpecialChar = ['%', '@', '$', '"', '-', '_']
        lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        upper_alphabet = 'ABCEDFGHIJKLMNOPQRSTUVWXYZ'

        if any(i in specialChar for i in data["username"]):
            raise serializers.ValidationError("name is not contain Special Character")

        if data['username']:
            if User.objects.filter(username=data['username']).exists():
                raise serializers.ValidationError('username is taken')
        if data['email']:
            if User.objects.filter(email=data['email']).exists():
                raise serializers.ValidationError('email is taken')

        if not len(data['password']) >= 8:
            raise serializers.ValidationError('Password should be eight Char')

        if not any(i in upper_alphabet for i in data['password']):
            raise serializers.ValidationError("Password should be one upper case")

        if not any(i in lower_alphabet for i in data['password']):
            raise serializers.ValidationError('password should be one lower case')

        if not any(i in numeric for i in data['password']):
            raise serializers.ValidationError('password at least one numeric')

        if not any(i in validSpecialChar for i in data['password']):
            raise serializers.ValidationError(f"({validSpecialChar})password should be contain special char")

        return data

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'], email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return validated_data
