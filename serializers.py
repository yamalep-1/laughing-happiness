from rest_framework import serializers
from .models import Note, Tag, NoteDetails

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']

class NoteDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NoteDetails
        fields = ['is_important', 'priority_level']

class NoteSerializer(serializers.ModelSerializer):
    details = NoteDetailsSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Note
        fields = ['id', 'user', 'content', 'created_at', 'details', 'tags']
        read_only_fields = ['user']
