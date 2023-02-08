from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self):
        cleaned_date = super().clean()
        username = cleaned_date.get('username')
        password = cleaned_date.get('password')

        try:
            self.user = User.objects.get(username=username)
        except User.DoesNotExist:
            raise forms.ValidationError(f'The user with {username} was not exist!')
        if not self.user.check_password(password):
            raise forms.ValidationError(f'Password for user {username} is not correct!')


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].requared = True
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widget = {
            'password': forms.PasswordInput
        }

