from django import forms
from .models import CommitteeInfo


class CommitteeCreateForms(forms.ModelForm):
    class Meta:
        model = CommitteeInfo
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'file-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'designation': forms.TextInput(attrs={'class': 'form-control'}),

        }
