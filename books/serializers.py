from rest_framework import serializers
from .models import Book, ReadingListItem, ReadingList

class BookSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.ReadOnlyField(source='uploaded_by.username')
    
    class Meta:
        model = Book
        fields = "__all__"
        read_only_fields = ["uploaded_by, 'uploaded_at"]
        
class ReadingListItemSerializer(serializers.ModelSerializer):
    book_title = serializers.ReadOnlyField(source='book.title')
    
    class Meta:
        model = ReadingListItem
        fields = ['id', 'book', 'book_title', 'order']
        
class ReadingListSerializer(serializers.ModelSerializer):
    items = ReadingListItemSerializer(many=True, read_only=True)
    
    class Meta:
        model = ReadingList
        fields = ['id', 'name', 'created_at', 'items']