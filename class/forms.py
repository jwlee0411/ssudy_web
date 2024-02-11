from django import forms
from .models import Reserve, Check

class CheckForm(forms.ModelForm):
    model = Check
    fields = ('checksum',)


class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        # fields = ('title', 'contents', 'board')

        fields = ('space', 'date', 'description', 'people')

