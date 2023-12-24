from core.models import Category, Finalist, Episodes, Services, Post
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class FinalistSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Finalist
        fields = ['id', 'name', 'votes', 'category', 'image']


class EpisodesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Episodes
        fields = ['id', 'name', 'link', 'image']


class ServicesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Services
        fields = ['id', 'name', 'description', 'image']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }