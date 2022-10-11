from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=True, label='Summary', queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'type': widgets.CheckboxSelectMultiple
        }

