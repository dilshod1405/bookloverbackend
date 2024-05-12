from rest_framework import serializers

from .models import Book, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')
        

class BookDetailsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'description', 'read_count', 'pages', 'picture', 'downloading_url', 'category', 'created_at')
        
    

class BooksListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Book
        fields = ('id', 'name', 'author', 'read_count', 'picture', 'category', 'created_at', 'recommended', 'downloading_url')


class BookReadCountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('read_count',)
