from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['username'] = user.username
        # ...

        return token




class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name",'access']

    def create(self, validated_data):
        username = validated_data["username"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        new_user = User(username=username, first_name=first_name,last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        validated_data['access'] = MyTokenObtainPairSerializer.get_token(new_user)
        return validated_data



class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(allow_blank=True, read_only=True)
    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")

        try:
            user = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("This username does not exist")

        if not user.check_password(my_password):
            raise serializers.ValidationError("Incorrect username/password combination!")

        payload = MyTokenObtainPairSerializer.get_token(user)
        token = str(payload.access_token)

        data["access"] = token
        return data
