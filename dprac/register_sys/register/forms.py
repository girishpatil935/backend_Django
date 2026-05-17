from django import forms
from .models import UserName, Skill
class UserNameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ['user', 'skill_name']