from rest_framework import generics, permissions
from .models import Book, ReadingList, ReadingListItem
from .serializers import BookSerializer, ReadingListSerializer, ReadingListItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)
        
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
class ReadingListView(generics.ListCreateAPIView):
    serializer_class = ReadingListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class ReadingListDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReadingListSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        return ReadingList.objects.filter(user=self.request.user)
    
    
class ReadingListItemView(generics.CreateAPIView):
    serializer_class = ReadingListItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def perform_create(self, serializer):
        reading_list_id = self.kwargs['pk']
        reading_list = ReadingList.objects.get(pk=reading_list_id, user=self.request.user)
        serializer.save(reading_list=reading_list)
        
    
class RemoveBookFromReadingListView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, list_pk, book_pk):
        try:
            item = ReadingListItem.objects.get(
                reading_list__id=list_pk,
                reading_list__user=request.user,
                book__id=book_pk
            )
            item.delete()
            return Response({'message': 'Book removed from reading list'}, status=status.HTTP_204_NO_CONTENT)
        except ReadingListItem.DoesNotExist:
            return Response({'error': 'Book not found in this reading list'}, status=status.HTTP_404_NOT_FOUND)


