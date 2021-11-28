from user_mbe.models import User

from typing import Dict

from rest_framework import serializers


class UserRegistrationSerializer(serializers.ModelSerializer):
    id                  = serializers.IntegerField(read_only=True)

    username            = serializers.CharField(max_length=150)
    password            = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = [
            "id",

            "username",
            "password"
        ]

    def validate_username(self, value: str):

        if User.objects.filter(username=value).exists():

            # raise error
            raise serializers.ValidationError(f"User with username: {value} already exists!")

        return value

    def create(self, validated_data: Dict):

        # Creating an Object of User Model
        obj = User(username=validated_data.get("username"))
        # Setting Password
        obj.set_password(validated_data["password"])
        # Saving the Instance
        obj.save()

        # Returning the Saved User Instance
        return obj
