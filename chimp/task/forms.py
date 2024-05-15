from .models import Resolve
from django.forms import ModelForm, TextInput, Textarea, HiddenInput

class ResolveForm(ModelForm):
    class Meta:
        model = Resolve
        fields = ["resolve", "user_id", "task_id", "decision_status", "resolve_date"]
        widgets = {
            "resolve": Textarea(attrs = {
            'class': 'text-field',
            'placeholder': 'Введите решение',
            'cols' :'80',
            'rows':'5',}),

            "user_id": HiddenInput(attrs={
                'value' : 'userId001'
            }),
            "task_id": HiddenInput(attrs={
                'value' : 'taskId023'
            }),
            "decision_status": HiddenInput(attrs={
                'value' : '-'
            }),
            "resolve_date": HiddenInput(attrs={
                'value' : '-'
            }),
            "resolve_language": HiddenInput(attrs={
                'value' : 'Python'
            }),
            


    }