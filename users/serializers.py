from rest_framework import serializers
from .models import Skill
from django.contrib.auth.models import User

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password']

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )

        return user
    
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']

def validate_name(self, value):

    if Skill.objects.filter(name=value).exists():
        raise serializers.ValidationError(
            "This skill already exists."
        )

    if len(value) < 3:
        raise serializers.ValidationError(
            "Skill name must be at least 3 characters long."
        )

    return value