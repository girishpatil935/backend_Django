from rest_framework import serializers
from .models import Skill
from .models import Book

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

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'pages']
    
    def validate_title(self,value):
        if len(value)<3:
            raise serializers.ValidationError(
                "title must be at least 3 characters long."
            )
        return value
    def validate_pages(self,value):
        if value < 0:
            raise serializers.ValidationError(
                "no.of pages must be greater than zero."
            )
        return value
