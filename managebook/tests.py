from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from managebook.models import Book


class TestBook(APITestCase):
    def test_create(self):
        url = reverse('create')
        data = {
            'title': 'test title',
            'text': 'text',
            'user': 1
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # count_book = Book.objects.all().count()
        # self.assertEqual(count_book, 1)
        # response = self.client.get(url, data=data)
        # self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete(self):
        book = Book.objects.create(title='test title', text='test text')
        url = reverse('delete', kwargs={'title': book.title})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        count_book = Book.objects.all().count()
        self.assertEqual(count_book, 0)

    def test_list(self):
        book_1 = Book(title='test title1', text='test text1')
        book_2 = Book(title='test title2', text='test text2')
        Book.objects.bulk_create([book_1, book_2])
        url = reverse('list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()[0]['title'], 'test title1')
        self.assertEqual(response.json()[1]['text'], 'test text2')

        # count_book = Book.objects.all().count()
        # self.assertEqual(count_book, 2)

    def test_update(self):
        book = Book.objects.create(title='test title', text='test text')
        url = reverse('update', kwargs={'id': book.id})
        data = {
            'title': 'updated title',
            'text': 'updated text'
        }
        response = self.client.put(url, data, format='json')
        print(response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data.pop('title')
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Create your tests here.WEF
