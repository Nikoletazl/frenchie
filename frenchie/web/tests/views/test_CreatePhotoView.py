from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import  TestCase
from django.urls import reverse

from frenchie.web.models import AlbumPhoto


class CreatePhotoViewTests(TestCase):
    VALID_PHOTO_DATA = {
        'name': 'Ariya',
        'age': 1,
        'image': SimpleUploadedFile(name='test_image.png', content=open('static/images/Frenchie_getty627306148.png', 'rb').read(), content_type='image/png'),
    }

    def test_create_photo__expect_to_create(self):
        UserModel = get_user_model()
        self.user = UserModel.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        self.client.post(
            reverse('create photo'),
            data=self.VALID_PHOTO_DATA,
        )

        photo = AlbumPhoto.objects.first()

        self.assertIsNotNone(photo)
        self.assertEqual(self.VALID_PHOTO_DATA['name'], photo.name)
        self.assertEqual(self.VALID_PHOTO_DATA['age'], photo.age)
        self.assertEqual(self.VALID_PHOTO_DATA['image'], photo.image)


    def test_create_photo__when_all_valid__expect_to_redirect_to_home(self):
        UserModel = get_user_model()
        self.user = UserModel.objects.create_user(username='testuser', password='12345')
        login = self.client.login(username='testuser', password='12345')

        response = self.client.post(
            reverse('create photo'),
            data=self.VALID_PHOTO_DATA,
        )

        photo = AlbumPhoto.objects.first()

        expected_url = reverse('home page')
        self.assertRedirects(response, expected_url)


    def test_get__expect_correct_template(self):
        response = self.client.get(reverse('create photo'))

        self.assertTemplateUsed(response, 'album/photo_create.html')