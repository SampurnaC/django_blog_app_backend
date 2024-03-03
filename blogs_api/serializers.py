from rest_framework import serializers
from .models import Blog, Category

class BlogSerializer(serializers.ModelSerializer):
    # category = serializers.CharField(source='category.id', read_only=False)
    # category = serializers.CharField(many=False, read_only=False)
    # category_name = serializers.CharField(source="category.name", read_only=True)
    class Meta:
        model = Blog
        fields = ['name','description', 'category']
    def to_representation(self, obj):
        return {
            "name": obj.name,
            "description": obj.description,
            "category": obj.category.name
        }
       
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
