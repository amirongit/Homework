from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name',
                  'last_name', 'email', 'user_type')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None

    first_name = forms.CharField(label='First Name', max_length=150,
                                 required=True)
    last_name = forms.CharField(label='Last Name', max_length=150,
                                required=True)
    email = forms.EmailField(label='Email', max_length=254, required=True)
