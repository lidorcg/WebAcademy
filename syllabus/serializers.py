from rest_framework import serializers

from .models import Course, Module, Content, Concept, Type


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('title', 'description', 'prerequisites', 'requirements',)


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ('course', 'title', 'description', 'order',)


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('module', 'title', 'description', 'type', 'time', 'concepts', 'requirements', 'order', 'done',)


class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Concept
        fields = ('name', 'covered',)


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('name',)
