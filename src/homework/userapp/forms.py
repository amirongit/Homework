from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, required=True)
    first_name = forms.CharField(label='First Name', max_length=64,
                                 required=True)
    last_name = forms.CharField(label='Last Name', max_length=64,
                                required=True)
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput,
                               required=True)
    user_type = forms.ChoiceField(label='Role', choices=[('t', 'Teacher'),
                                                         ('s', 'Student')])
