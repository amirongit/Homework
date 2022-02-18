from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(label='Username', max_length=32, required=True)
    name = forms.CharField(label='Name', max_length=128, required=True)

    user_type = forms.ChoiceField(label='Role', choices=[('t', 'Teacher'), ('s', 'Student')])
