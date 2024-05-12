from django.test import TestCase
from .serializers import BookDetailsSerializer, BooksListSerializer, CategorySerializer, BookReadCountsSerializer
from .models import Book, Category
from rest_framework.test import APIClient


class BookDetailsSerializerTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=0, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
    
    def test_serializer(self):
        data = BookDetailsSerializer(self.book).data
        assert data['id'] == self.book.id
        assert data['name'] == self.book.name
        assert data['author'] == self.book.author
        assert data['description'] == self.book.description
        assert data['read_count'] == self.book.read_count
        assert data['pages'] == self.book.pages
        assert data['picture'] == self.book.picture.url
        assert data['downloading_url'] == self.book.downloading_url
        assert data['category']['name'] == self.book.category.name
        assert data['created_at'] == self.book.created_at.astimezone().isoformat()


class BooksListSerializerTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=0, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
    
    def test_serializer(self):
        data = BooksListSerializer(self.book).data
        assert data['id'] == self.book.id
        assert data['name'] == self.book.name
        assert data['author'] == self.book.author
        assert data['read_count'] == self.book.read_count
        assert data['picture'] == self.book.picture.url
        assert data['category']['name'] == self.book.category.name
        assert data['created_at'] == self.book.created_at.astimezone().isoformat()


class BookReadCountsSerializerTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=0, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
    
    def test_serializer(self):
        data = BookReadCountsSerializer(self.book).data
        assert data['read_count'] == self.book.read_count
        
        
class CategorySerializerTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='test')
    
    def test_serializer(self):
        data = CategorySerializer(self.category).data
        assert data['name'] == self.category.name


class BookDetailsViewTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=0, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
        self.client = APIClient()
        
    def test_view(self):
        response = self.client.get(f'/books/{self.book.id}/')
        self.assertEqual(response.status_code, 200)


class BooksListViewTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=0, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
        self.client = APIClient()
    
    def test_view(self):
        response = self.client.get('/all_books/')
        self.assertEqual(response.status_code, 200)


class CategoryViewTest(TestCase):
    def setUp(self) -> None:
        self.category = Category.objects.create(name='test')
        self.client = APIClient()
    
    def test_view(self):
        response = self.client.get(f'/categories/')
        self.assertEqual(response.status_code, 200)


class BookReadCountsViewTest(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(name='test', author='test', description='test', read_count=3, pages=1, picture='test', downloading_url='test', category=Category.objects.create(name='test'), created_at='test')
        self.client = APIClient()
    
    def test_view(self):
        response = self.client.post(f'/book/{self.book.id}/')
        self.assertEqual(response.status_code, 200)

