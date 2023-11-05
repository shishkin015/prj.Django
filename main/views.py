from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


class StudentListView(ListView):
    model = Student
    extra_context = {
        'title': 'Студенты'
    }


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} ({email}): {message}')

    context = {
        'title': 'Контакт'
    }
    return render(request, 'main/contact.html', context)


class StudentDetailView(DetailView):
    model = Student
    extra_context = {
        'title': 'Студент'
    }


class StudentCreateView(CreateView):
    model = Student
    # fields = ('first_nami', 'last_name', 'avatar', 'is_active',)
    # заменили на
    form_class = StudentForm

    extra_context = {
        'title': 'Добавить студента'
    }

    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    # fields = ('first_nami', 'last_name', 'avatar', 'is_active',)
    # заменили на
    form_class = StudentForm

    extra_context = {
        'title': 'Обновить студента'
    }

    success_url = reverse_lazy('main:index')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # Формирование формсета
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)  # получаем данные
        else:
            context_data['formset'] = SubjectFormset(instance=self.object)  # отправляем данные
        return context_data

    def form_valid(self, form):
        # обрабатываем полученные данные, проверяем и сохраняем
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


class StudentDeleteView(DeleteView):
    model = Student
    extra_context = {
        'title': 'Удалить студента'
    }
    success_url = reverse_lazy('main:index')


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    student_item.is_active = False if student_item.is_active else True

    student_item.save()

    return redirect(reverse('main:index'))
