from django import forms
from user.models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'bio', 'location', 'date_of_birth', 'gender']
        widgets = {
            'bio': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Write a short bio',
                'class': 'input-field',
            }),
            'location': forms.TextInput(attrs={
                'placeholder': 'City, Country',
                'class': 'input-field',
            }),
            'date_of_birth': forms.DateInput(attrs={
                'type': 'date',
                'class': 'input-field',
            }),
            'gender': forms.Select(attrs={
                'class': 'input-field',
            }),
        }
