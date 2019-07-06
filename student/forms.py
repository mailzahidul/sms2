from django import forms
from .models import StudentClassInfo, StudentShiftInfo, StudentInfo, StudentDetailInfo
from teachers.models import TecherInfo


class StudentSearch(forms.Form):
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all())
    roll = forms.IntegerField(required=False)


class StudentRegistrationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    roll = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    contact_number = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    reference_teacher = forms.ModelChoiceField(queryset=TecherInfo.objects.all())
    std_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all())
    std_shift = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all())
    std_section = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all())


# class StudentCreateForm(forms.ModelForm):
#     class Meta:
#         model = StudentInfo
#         fields = '__all__'
#
#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
#             'roll': forms.IntegerField(attrs={'class': 'form-control', 'placeholder': 'Student Roll'}),
#             'father_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father Name'}),
#             'mother_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother Name'}),
#             'contact_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Contact No.'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address'}),
#             'reference_teacher': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Student Name'}),
#         }

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Student Name'})
        }

class StudentDetailInfoForm(forms.ModelForm):
    class Meta:
        model = StudentDetailInfo
        exclude = ('student',)
