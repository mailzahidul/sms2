from django.shortcuts import render, redirect
from .forms import StaffRegistrationForm
from .models import StaffRegistration


# Create your views here.
def staff_registration(request):
    forms = StaffRegistrationForm()
    if request.method == 'POST':
        forms = StaffRegistrationForm(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('staff-list')
    return render(request, 'staff/registration.html', context={'forms': forms})


def staff_list(request):
    staff = StaffRegistration.objects.all().order_by('-id')
    context = {'staff': staff}
    return render(request, 'staff/staff_list.html', context)


def staff_details(request, staff_id):
    staff = StaffRegistration.objects.get(id=staff_id)
    context = {'staff': staff}
    return render(request, 'staff/staff_details.html', context)


def delete_staff(request, staff_id):
    staff = StaffRegistration.objects.get(id=staff_id)
    staff.delete()
    return redirect('staff-list')


def edit_staff(request, staff_id):
    staff = StaffRegistration.objects.get(id=staff_id)
    forms1 = StaffRegistrationForm(instance=staff)
    if request.method == 'POST':
        forms1 = StaffRegistrationForm(request.POST, instance=staff)
        if forms1.is_valid():
            forms1.save()
            return redirect('staff-list')
    return render(request, 'staff/edit_staff.html', {'forms': forms1})
