from django.db import models
from django.core.validators import MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=255)
    
    
    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.name
    


class Book(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateField(auto_now=True)
    read_count = models.IntegerField(default=0)
    pages = models.IntegerField(validators=[MinValueValidator(1)])
    picture = models.ImageField()
    downloading_url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    recommended = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'books'

    
    def __str__(self):
        return f'{self.name} {self.category}'

