from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    CHOICES = [
        ('new', 'New'),
        ("in_the_process", 'In the process'),
        ("made", 'Made')
    ]

    description = forms.CharField(max_length=300, required=True, label='Description')
    detail_description = forms.CharField(max_length=3000, required=False, label='Detail description', widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Status', choices=CHOICES)
    execute_at = forms.DateField(required=False, label='Execute at', widget=forms.widgets.DateInput(attrs={'type': 'date'}))

