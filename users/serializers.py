from rest_framework import serializers
from .models import Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name', 'user']

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