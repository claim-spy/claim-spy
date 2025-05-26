from back.claimspy.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        depth = 1
        fields = "all"
        extra_kwargs = {
            'password': {'write_only': True},
            'id': {'read_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop("password")
        role = validated_data.get('role')

        # Create the User instance
        user = User(**validated_data)
        user.set_password(password)
        user.full_clean()
        
        if role == "admin":
            user.is_staff = True
        
        user.save()

        return user

