from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class UserInfoForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'user_type')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        for field in ['username', 'password1', 'password2']:
            self.fields[field].help_text = None
        for field in list(set(self.fields) - {'user_type'}):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['user_type'].widget.attrs.update({'class': 'form-select'})

    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)
    email = forms.EmailField(max_length=254, required=True)


class SignInForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in list(set(self.fields) - {'user_type'}):
            self.fields[field].widget.attrs.update({'class': 'form-control'})
        self.fields['username'].widget.attrs.update({'autofocus': False})
