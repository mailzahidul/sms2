from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import EmployeeCreateForm


# Create your views here.
def create_employee(request):
    forms = EmployeeCreateForm()
    if request.method == 'POST':
        forms = EmployeeCreateForm(request.POST)
        print(forms)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user_obj = User.objects.create_user(username=username, password=password)
            new_user = forms.save(commit=False)
            new_user.user = user_obj
            new_user.save()
            return redirect('employee-create')
    context = {'forms': forms}
    return render(request, 'administration/create_employee.html', context)
