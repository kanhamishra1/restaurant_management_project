from django import forms
from .models import Contact



class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def clean_message(self):
        message = self.cleaned_data.get("message")
        if len(massage) < 10:
            raise forms.ValidationError("Message must be at least 10 character long.")
        return message
         