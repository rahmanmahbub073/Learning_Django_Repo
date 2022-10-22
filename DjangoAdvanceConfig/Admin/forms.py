import email
from django import forms
from django.core import validators


class TeacherRegistration(forms.Form):
    first_name = forms.CharField(label='Enter the first name', label_suffix='')
    last_name = forms.CharField(initial='Rahman')
    email = forms.EmailField(
        initial='rahmanmahbub073@gmail.com', disabled=True)
    password = forms.CharField(widget=forms.PasswordInput)
    textarea = forms.CharField(widget=forms.Textarea)
    file = forms.ChoiceField(widget=forms.FileInput)
    checkbox = forms.CharField(widget=forms.CheckboxInput)

    def clean(self):
        clean_data = super().clean()
        rightpass = self.cleaned_data['password']
        wrongpass = self.cleaned_data['repass']
        if rightpass != wrongpass:
            raise forms.ValidationError("password doesnt match")
