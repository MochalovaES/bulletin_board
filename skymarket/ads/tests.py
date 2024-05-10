from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from ads.models import Ad, Comment
from users.models import User


class AdTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test', first_name='Test',
                                        last_name='Testov')
        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="Test",
            price=100,
            author=self.user,
            description="Test",
            created_at="2022-02-03T09:10:16.332479Z"
        )

    def test_create_ad(self):
        """Тестирование создания объявления"""
        data = {
            "title": "Test1",
            "price": 100,
            "author": self.user.pk,
            "description": "Test1",

        }

        response = self.client.post(
            path='/ads/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Ad.objects.all().exists()
        )

    def test_list_ads(self):
        """Тестирование вывода списка объявлений"""

        response = self.client.get(
            path='/ads/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Ad.objects.all().count(),
            1
        )

    def test_retrieve_ad(self):
        """Тестирования детальной информации об объявлении"""
        response = self.client.get(
            path=f'/ads/{self.ad.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.ad.pk,
                "author": self.user.pk,
                "author_first_name": "Test",
                "author_last_name": "Testov",
                "author_email": "test@example.com",
                "author_phone": None,
                "title": "Test",
                "price": 100,
                "description": "Test",
                "created_at": "2022-02-03T09:10:16.332479Z",
                "image": None,
            }
        )

    def test_update_ad(self):
        """Тестирование обновления объявления"""
        data = {
            "title": 'test_update'
        }

        response = self.client.patch(
            path=f'/ads/{self.ad.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title'],
            data['title']
        )

    def test_destroy_ad(self):
        """Тестирование удаления объявления"""
        response = self.client.delete(
            path=f'/ads/{self.ad.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )


class CommentTestCase(APITestCase):

    def setUp(self) -> None:
        self.client = APIClient()
        self.user = User.objects.create(email='test@example.com', password='test', first_name='Test',
                                        last_name='Testov')
        self.client.force_authenticate(user=self.user)

        self.ad = Ad.objects.create(
            title="Test",
            price=100,
            author=self.user,
            description="Test",
            created_at="2022-02-03T09:10:16.332479Z"
        )

        self.comment = Comment.objects.create(
            text="Test",
            author=self.user,
            ad=self.ad,
            created_at="2022-02-04T09:10:16.332479Z"
        )

    def test_create_comment(self):
        """Тестирование создания отзыва"""
        data = {
            "text": "Test1",
            "author": self.user.pk,
            "ad": self.ad.pk,
            "created_at": "2022-02-04T09:10:16.332479Z",

        }

        response = self.client.post(
            path=f'/ads/{self.ad.pk}/comments/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Comment.objects.all().exists()
        )

    def test_list_ads(self):
        """Тестирование вывода списка отзыва у объявления"""

        response = self.client.get(
            path=f'/ads/{self.ad.pk}/comments/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            Comment.objects.all().count(),
            1
        )

    def test_retrieve_comment(self):
        """Тестирования детальной информации об отзыве"""
        response = self.client.get(
            path=f'/ads/{self.ad.pk}/comments/{self.comment.pk}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json(),
            {
                "id": self.comment.pk,
                "text": "Test",
                "ad": self.ad.pk,
                "author": self.user.pk,
                "author_first_name": "Test",
                "author_last_name": "Testov",
                "author_image": '',
                "created_at": "2022-02-04T09:10:16.332479Z",
            }
        )

    def test_update_comment(self):
        """Тестирование обновления отзыва"""
        data = {
            "text": 'test_update'
        }

        response = self.client.patch(
            path=f'/ads/{self.ad.pk}/comments/{self.comment.pk}/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['text'],
            data['text']
        )

    def test_destroy_comment(self):
        """Тестирование удаления отзыва"""
        response = self.client.delete(
            path=f'/ads/{self.ad.pk}/comments/{self.comment.pk}/',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
