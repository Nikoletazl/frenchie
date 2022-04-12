from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

from frenchie.auth_app.models import Customer
from frenchie.helpers.form_control import FormControl
from frenchie.web.models import AlbumPhoto


class CreateProfileForm(FormControl, auth_forms.UserCreationForm):
    name = forms.CharField(
        max_length=Customer.NAME_MAX_LENGTH,
    )
    picture = forms.ImageField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_form_control()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Customer(
            name=self.cleaned_data['name'],
            picture=self.cleaned_data['picture'],
            email=self.cleaned_data['email'],
            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'name', 'picture')
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
        }


class EditProfileForm(FormControl, forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your name',
                }
            ),
            'picture': forms.TextInput(
                attrs={
                    'placeholder': 'Enter URL',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter email',
                }
            ),
        }


class DeleteProfileForm(forms.ModelForm):
    def save(self, commit=True):
        # Not good
        # should be done with signals
        # because this breaks the abstraction of the auth app
        pets = list(self.instance.pet_set.all())
        AlbumPhoto.objects.all().delete()
        self.instance.delete()

        return self.instance

    class Meta:
        model = Customer
        fields = ()