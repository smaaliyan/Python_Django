from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ("title", "text")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={'class': 'form-control mb5'})
        }
        labels ={
            'text': 'Write you massage here:'
        }

    def clean_title(self):
        title = self.cleaned_data["title"]
        if "django " not in title.lower():
            raise ValidationError("We only accept notes about Django!")
        return title