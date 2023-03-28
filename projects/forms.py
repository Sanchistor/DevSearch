from django.forms import ModelForm
from .models import Project
from django import forms


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image',  'demo_link', 'source_link', 'tags']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs.update({'class': 'input', 'placeholder': 'Add title'})
        self.fields['description'].widget.attrs.update({'class': 'input', 'placeholder': 'Add description'})
        self.fields['demo_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add demo link'})
        self.fields['source_link'].widget.attrs.update({'class': 'input', 'placeholder': 'Add source link'})
