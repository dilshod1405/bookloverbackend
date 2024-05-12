from django.shortcuts import render
from rest_framework import viewsets, generics, status
from .models import Book, Category
from .serializers import BooksListSerializer, BookDetailsSerializer, CategorySerializer, BookReadCountsSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count
from django.http import JsonResponse

    
# View all books
class BooksListView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BooksListSerializer


# View single book
class BookDetailsView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookDetailsSerializer



class BookReadCountsView(APIView):
    def post(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
        book.read_count += 1
        book.save()
        
        serializer = BookReadCountsSerializer(book)
        return Response(serializer.data)
    
      
# View all categories
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    


def count_books_by_category_type(request):
    # Perform aggregation to count the number of books per category
    book_counts = Category.objects.annotate(num_books=Count('book')).values('name', 'num_books', 'id').order_by('id')
    
    # Convert QuerySet to list for easier serialization
    book_counts_list = list(book_counts)

    return JsonResponse(book_counts_list, safe=False)   