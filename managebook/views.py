from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.response import Response

from managebook.models import Book, Comment
from managebook.serialize import BookSerializerRead, CommentSerializer,BookSerializerWrite


class ListBook(ListAPIView):
    serializer_class = BookSerializerRead

    # queryset = Book.objects.all()
    # def get(self, request, id=None):
    #     if id is None:
    #         data = Book.objects.all()
    #         serialized_data = BookSerializer(data, many=True)
    #         return Response(serialized_data.data)
    #     data = Book.objects.get(id=id)
    #     serialized_data = BookSerializer(data)
    #     return Response(serialized_data.data)

    def get_queryset(self):
        if self.kwargs.get('id'):
            return Book.objects.filter(id=self.kwargs.get('id'))
        return Book.objects.all()


class CreateBook(CreateAPIView):
    serializer_class = BookSerializerWrite


class DestroyBook(DestroyAPIView):
    # def get_object(self):
    #     return Book.objects.get(title=self.kwargs['title'])

    # lookup_field = 'id'
    # def get_queryset(self):
    #     return Book.objects.all()

    def delete(self, request, title):
        Book.objects.filter(title=title).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UpdateBook(UpdateAPIView):
    serializer_class = BookSerializerWrite

    def get_object(self):
        return Book.objects.get(id=self.kwargs.get('id'))

    # serializer_class = BookSerializer
    #
    # def put(self, request, title, text):
    #     # instance = self.get_object()
    #     Book.objects.get(title=title, text=text).update()
    #     return Response({'ok':True})
# Create your views here.


class ListComment(ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects
