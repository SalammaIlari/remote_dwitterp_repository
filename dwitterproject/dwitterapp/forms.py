from django import forms
from multiselectfield import MultiSelectFormField
class AccountForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )

    email = forms.EmailField(
        label="Enter your email",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email'
            }
        )
    )
    contact_no = forms.IntegerField(
        label="Enter your contact_no",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your contact_no'
            }
        )
    )
    describe_yourself = forms.CharField(
        label="describe yourself",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'describe yourself'
            }
        )
    )
    choose_a_profile_picture=forms.ImageField(
        label="create a profile yourself",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'profile picture'
            }
        )
    )
    What_are_you_interested_in=forms.CharField(
        label="interested hobbies",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'interested hobbies'
            }
        )
    )
    LANGUAGES_CHOICES = (
        ('Eng', 'English'),
        ('Tel', 'Telugu'),
        ('Hin', 'Hindi'),
        ('Kan', 'Kannada'),
    )
    Preferred_Languages = MultiSelectFormField(max_length=150, choices=LANGUAGES_CHOICES)
class test2(forms.Form):
    Username = forms.CharField(
        label="Enter your email",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': ' your email'
            }
        )
    )
    password = forms.IntegerField(
        label="Enter your password",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your password'
            }
        )
    )
