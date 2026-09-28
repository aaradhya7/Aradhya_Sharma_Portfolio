from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ["name", "email", "subject", "message"]

        widgets = {
            "name": forms.TextInput(attrs={
                "placeholder": "Your name",
                "class": "contact-input"
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Your email",
                "class": "contact-input"
            }),
            "subject": forms.TextInput(attrs={
                "placeholder": "Subject",
                "class": "contact-input"
            }),
            "message": forms.Textarea(attrs={
                "placeholder": "Write your message...",
                "class": "contact-input",
                "rows": 5
            }),
        }