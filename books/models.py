from django.db import models
from django.conf import settings

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    publication_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='books'
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class ReadingList(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='reading_lists'
    )
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def ___str__(self):
        return f"{self.name} ({self.user.username})"
    
class ReadingListItem(models.Model):
    reading_list = models.ForeignKey(
        ReadingList, 
        on_delete=models.CASCADE,
        related_name='items'
    )
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    order = models.PositiveBigIntegerField()
    
    class Meta:
        unique_together = ('reading_list', 'book')
        ordering = ['order']
        
    def __str__(self):
        return f"{self.book.title} in {self.reading_list.name}"