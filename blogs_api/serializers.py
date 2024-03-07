from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.id', read_only=False)
    # category = serializers.CharField(many=False, read_only=False)
    # category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
    def to_representation(self, obj):
        return {
            "id": obj.id,
            "name": obj.name,
            "description": obj.description,
            "category": obj.category.name,
            "image": obj.image.url,
            "artist": obj.artist,
        }
       
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
