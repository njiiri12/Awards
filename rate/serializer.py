from rest_framework import serializers
from .models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ('title', 'description','image', 'link', 'profile', 'pubdate')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'picture', 'email', 'github_link')