from django import forms
from django.forms import widgets
from webapp.models import Type, Status, Task
from webapp.models.projects import Project
from webapp.widgets import DatePickerInput


class TaskForm(forms.ModelForm):
    status = forms.ModelChoiceField(required=True, label='Summary', queryset=Status.objects.all())

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'type')
        widgets = {
            'type': widgets.CheckboxSelectMultiple
        }


class ProjectForm(forms.ModelForm):
    beginning_date = forms.DateField(required=True, label='Beginning date', widget=DatePickerInput)
    expiration_date = forms.DateField(required=False, label='Expiration date', widget=DatePickerInput)

    class Meta:
        model = Project
        fields = ('title', 'description', 'beginning_date', 'expiration_date')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Search")

