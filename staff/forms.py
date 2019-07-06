from django import forms
from .models import StaffRegistration


class StaffRegistrationForm(forms.ModelForm):
    class Meta:
        model = StaffRegistration
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'father_name': forms.TextInput(attrs={'class': 'form-control'}),
            'mother_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'joining_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }
    # name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # mother_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # dob = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    #                       label="Date Of Birth:")
    # gender_choice = (
    #     ('m', 'Male'),
    #     ('f', 'Female'),
    # )
    # gender = forms.ChoiceField(choices=gender_choice, widget=forms.Select(attrs={'class': 'form-control'}))
    # joining_date = forms.DateField(initial=datetime.date.today(),
    #                                widget=forms.TextInput(attrs={'class': 'form-control', 'type':'date'}))
    # address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    # photo = forms.ImageField()
    # contact = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
