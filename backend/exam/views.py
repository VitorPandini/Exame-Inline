from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import CareForm, CareItemsFormset
from .models import Care, CareItems, Exam


def care_list(request):
    template_name = 'exam/care_list.html'
    object_list = Care.objects.all()
    context = {'object_list': object_list}
    return render(request, template_name, context)


def care_create(request):
    template_name = 'exam/care_create.html'
    form = CareForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            # Salva o atendimento
            care = form.save()
            exams = Exam.objects.all()
            aux = []
            for exam in exams:
                care_items = CareItems(
                    care=care,
                    exam=exam
                )
                aux.append(care_items)
            CareItems.objects.bulk_create(aux)

            return redirect('exam:care_list')

    context = {'form': form}
    return render(request, template_name, context)


def care_detail(request, pk):
    template_name = 'exam/care_detail.html'
    obj = Care.objects.get(pk=pk)
    context = {'object': obj}
    return render(request, template_name, context)


def care_update(request, pk):
    template_name = 'exam/care_update.html'
    care_instance = Care.objects.get(pk=pk)

    form = CareForm(request.POST or None, instance=care_instance, prefix='main')
    formset = CareItemsFormset(request.POST or None, instance=care_instance, prefix='items')

    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def care_update_exam(request, pk):
    '''
    Atualiza cada exame marcando is_done como True ou False.
    '''
    care_items = CareItems.objects.get(pk=pk)
    # Verifica se a lista com os valores do request tem alguma coisa ou
    # se a lista vem vazia.
    is_done_list = list(request.GET.values())

    if is_done_list:
        is_done = True
    else:
        is_done = False

    care_items.is_done = is_done
    care_items.save()
    return HttpResponse(pk)
