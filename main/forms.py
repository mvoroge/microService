from .models import direct
from django.forms import ModelForm, TextInput, FileInput


class directForm(ModelForm):
    class Meta:
        model = direct
        fields = ["titleFile", "samFile"]
        widgets = {
            "titleFile": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
                'style': "padding: 10px"
            }),
            "samFile": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Добавить...'
            }),
        }
