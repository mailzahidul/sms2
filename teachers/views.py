from django.shortcuts import render, redirect
from .forms import CreateTeacherForm
from .models import TecherInfo


def create_teacher(request):
    forms = CreateTeacherForm()
    if request.method == 'POST':
        forms = CreateTeacherForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
            # TecherInfo.objects.create(
            #     name=forms.cleaned_data['name'],
            #     gender=forms.cleaned_data['gender'],
            #     age=forms.cleaned_data['age'],
            #     phone=forms.cleaned_data['phone'],
            #     designation=forms.cleaned_data['designation']
            # )

    context = {'forms': forms}
    return render(request, 'teacher/create_teacher.html', context)


def teacher_list(request):
    teacher_obj = TecherInfo.objects.all()
    context = {'teacher_obj': teacher_obj}
    return render(request, 'teacher/teacher_list.html', context)


def teacher_edit(request, teacher_id):
    teacher_obj = TecherInfo.objects.get(id=teacher_id)
    forms = CreateTeacherForm(instance=teacher_obj)
    if request.method == 'POST':
        forms = CreateTeacherForm(request.POST, instance=teacher_obj)
        if forms.is_valid():
            forms.save()
            return redirect('teacher-list')
    context = {'forms': forms}
    return render(request, 'teacher/edit_teacher.html', context)


def teacher_delete(request, teacher_id):
    teacher_obj = TecherInfo.objects.get(id=teacher_id)
    teacher_obj.delete()
    return redirect('teacher-list')
