from django import forms 
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User 


from django import forms
from django.contrib.auth.hashers import make_password
from .models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'age']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password_confirm and password != password_confirm:
            self.add_error('password_confirm', "Passwords do not match")

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.password = make_password(password)
        
        if commit:
            user.save()
        
        return user



class CustomUserChangeForm(UserChangeForm): 
    class Meta:
        model = User 
        fields = '__all__'