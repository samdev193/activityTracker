from django import  forms
from django.contrib.auth.forms import UserCreationForm, User


class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)  # Call to ModelForm constructor
        for field in self.fields:
            self.fields[field].widget.attrs["required"] = "required"


