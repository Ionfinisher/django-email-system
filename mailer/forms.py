from django import forms


class ContactForm(forms.Form):
    email = forms.EmailField(label="Votre Email")
    message = forms.CharField(label="Votre message", widget=forms.Textarea)
