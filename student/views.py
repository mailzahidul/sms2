from django.shortcuts import render, redirect
from .forms import StudentRegistrationForm, StudentSearch, StudentInfoForm, StudentDetailInfoForm
from .models import *
from django.contrib.auth.decorators import login_required


def attendance_count(request):
    class_name = request.GET.get('class_name', None)
    if class_name:
        stu_list = StudentDetailInfo.objects.filter(
            std_class__class_short_form=class_name).order_by('roll')
        context = {'stu_list': stu_list}
    else:
        context = {}
    return render(request, 'student/attendance_count.html', context)


@login_required
def create_student(request):
    forms = StudentRegistrationForm()
    if request.method == 'POST':
        forms = StudentRegistrationForm(request.POST)
        if forms.is_valid():
            std_name = forms.cleaned_data['name']
            std_roll = forms.cleaned_data['roll']
            std_father_name = forms.cleaned_data['father_name']
            std_mother_name = forms.cleaned_data['mother_name']
            std_contact_number = forms.cleaned_data['contact_number']
            std_address = forms.cleaned_data['address']
            std_reference_teacher = forms.cleaned_data['reference_teacher']
            std_std_class = forms.cleaned_data['std_class']
            std_std_shift = forms.cleaned_data['std_shift']

            try:
                std_obj = StudentInfo.objects.create(
                    name=std_name,
                    roll=std_roll,
                    father_name=std_father_name,
                    mother_name=std_mother_name,
                    contact_number=std_contact_number,
                    address=std_address,
                    reference_teacher=std_reference_teacher
                )
                StudentDetailInfo.objects.create(
                    student=std_obj,
                    std_class=std_std_class,
                    std_shift=std_std_shift
                )
            except Exception as err:
                print(err)
            return redirect('student-list')
    context = {'forms': forms}
    return render(request, 'student/create_student.html', context)


def register_student(request):
    forms1 = StudentInfoForm(request.POST or None)
    forms2 = StudentDetailInfoForm(request.POST or None)
    if request.method == 'POST':
        if forms1.is_valid() and forms2.is_valid():
            stu_obj = forms1.save()
            stu_detail = forms2.save(commit=False)
            stu_detail.student = stu_obj
            stu_detail.save()
            return redirect('student-list')
    context = {'forms1': forms1, 'forms2': forms2}
    return render(request, 'student/register_student.html', context)


def student_list(request):
    stu_obj = StudentDetailInfo.objects.all()
    context = {'students': stu_obj}
    return render(request, 'student/student_list.html', context)


def student_edit(request, student_id):
    std_obj1 = StudentDetailInfo.objects.get(id=student_id)
    std_obj2 = std_obj1.student

    forms2 = StudentDetailInfoForm(request.POST or None, instance=std_obj1)
    forms1 = StudentInfoForm(request.POST or None, instance=std_obj2)
    if request.method == 'POST':
        if forms1.is_valid() and forms2.is_valid():
            st = forms1.save()
            st2 = forms2.save(commit=False)
            st2.student = st
            st2.save()
            return redirect('student-list')
    context = {'forms1': forms1, 'forms2': forms2}
    return render(request, 'student/student_edit.html', context)


def student_delete(request, student_id):
    std_obj = StudentInfo.objects.get(id=student_id)
    std_obj.delete()
    return redirect('student-list')


def student_detail(request, student_id):
    std_obj2 = StudentDetailInfo.objects.get(id=student_id)
    std_obj1 = std_obj2.student
    context = {'student1': std_obj1, 'student2': std_obj2}
    return render(request, 'student/student_details.html', context)


def student_search(request):
    forms = StudentSearch()
    stu_class = request.GET.get('std_class', None)
    print(stu_class)
    stu_roll = request.GET.get('roll', None)
    if stu_class:
        students = StudentDetailInfo.objects.filter(stu_class__id=stu_class)
        print(students)
    context = {'forms': forms}
    return render(request, 'student/student_search.html', context)


