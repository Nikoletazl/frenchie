from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import  TestCase

from frenchie.web.models import AlbumPhoto


class AlbumPhotoTest(TestCase):
    VALID_PHOTO_DATA = {
        'name': 'Ariya',
        'age': 1,
        'image': SimpleUploadedFile(name='test_image.png',
                                    content=open('static/images/Frenchie_getty627306148.png', 'rb').read(),
                                    content_type='image/png'),
    }

    def test_create_photo_when_age_is_negative__expect_to_fail(self):
        age = -1

        photo = AlbumPhoto(
            name=self.VALID_PHOTO_DATA['name'],
            age=age,
            image=self.VALID_PHOTO_DATA['image'],
        )

        with self.assertRaises(ValidationError) as context:
            photo.full_clean()
            photo.save()

        self.assertIsNotNone(context.exception)

    def test_create_photo_when_name_is_less_than_2__expect_to_fail(self):
        name = 'a'

        photo = AlbumPhoto(
            name=name,
            age=self.VALID_PHOTO_DATA['age'],
            image=self.VALID_PHOTO_DATA['image'],
        )

        with self.assertRaises(ValidationError) as context:
            photo.full_clean()
            photo.save()

        self.assertIsNotNone(context.exception)