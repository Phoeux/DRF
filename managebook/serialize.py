from rest_framework.serializers import ModelSerializer

from managebook.models import Book, Comment
from django.contrib.auth.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class BookSerializerRead(ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Book
        fields = '__all__'


class BookSerializerWrite(ModelSerializer):

    class Meta:
        model = Book
        fields = '__all__'


class CommentSerializer(ModelSerializer):
    book = BookSerializerRead()
    user = UserSerializer()

    class Meta:
        model = Comment
        fields = '__all__'
