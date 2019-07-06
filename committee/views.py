from django.shortcuts import render, redirect
from .forms import CommitteeCreateForms
from .models import CommitteeInfo


def create_comt(request):
    forms = CommitteeCreateForms()
    if request.method == 'POST':
        forms = CommitteeCreateForms(request.POST, request.FILES)
        if forms.is_valid():
            forms.save()
            return redirect('comt-list')
    context = {'forms': forms}
    return render(request, 'committee/comt_create.html', context)


def comt_list(request):
    comt_obj = CommitteeInfo.objects.all()
    context = {'committee': comt_obj}
    return render(request, 'committee/comt_list.html', context)


def edit_comt(request, comt_id):
    comt_obj = CommitteeInfo.objects.get(id=comt_id)
    forms_obj = CommitteeCreateForms(instance=comt_obj)
    if request.method == 'POST':
        forms_obj = CommitteeCreateForms(request.POST, instance=comt_obj)
        if forms_obj.is_valid():
            forms_obj.save()
            return redirect('comt-list')
    return render(request, 'committee/comt_edit.html', {'forms': forms_obj})


def delete_comt(request, comt_id):
    comt_obj = CommitteeInfo.objects.get(id=comt_id)
    if request.method == 'POST':
        comt_obj.delete()
        return redirect('comt-list')
    return render(request, 'committee/comt_list.html')
