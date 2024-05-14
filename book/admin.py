from django.contrib import admin
from .models import Book, Category
from .serializers import BookDetailsSerializer



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    serializer_class = BookDetailsSerializer
    list_display = ('name', 'author', 'category', 'created_at', 'read_count', 'recommended','id')
    list_filter = ('category', 'created_at', 'author', 'recommended')
    search_fields = ('name', 'author', 'description', 'category__name', 'created_at')
    ordering = ('id',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')
    search_fields = ('name',)
    ordering = ('id',)
    
