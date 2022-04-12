from django import forms

from frenchie.helpers.disabled_fields import DisableFields
from frenchie.helpers.form_control import FormControl
from frenchie.web.models import AlbumPhoto


class CreatePhotoForm(forms.ModelForm, FormControl):
    class Meta:
        model = AlbumPhoto
        fields = ('name', 'description', 'age', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Enter your dog name",
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter a brief description for your dog'
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': "Enter your dog's age",
                },
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()


class EditPhotoForm(forms.ModelForm, FormControl):
    class Meta:
        model = AlbumPhoto
        fields = ('name', 'description', 'age', 'image')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': "Edit dog's name",
                },
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Edit description'
                },
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Edit age',
                },
            ),
        }


class DeletePhotoForm(forms.ModelForm, DisableFields):
    class Meta:
        model = AlbumPhoto
        fields = ('name', 'description', 'age', 'image')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_disabled_fields()

    def save(self, commit=True):
        self.instance.delete()
        return self.instance
