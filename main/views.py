from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.cache import cache
from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from pytils.translit import slugify

from config import settings
from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    extra_context = {
        'title': 'Студенты'
    }


@login_required
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


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    permission_required = 'main.view_student'
    extra_context = {
        'title': 'Студент'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            key = f'subject_list_{self.object.pk}'
            subject_list = cache.get(key)
            if subject_list is None:
                subject_list = self.object.subject_set.all()
                cache.set(key, subject_list)
        else:
            subject_list = self.object.subject_set.all()

        context_data['subjects'] = subject_list

        return context_data


class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Student
    # fields = ('first_nami', 'last_name', 'avatar', 'is_active',)
    # заменили на
    permission_required = 'main.add_student'
    form_class = StudentForm

    extra_context = {
        'title': 'Добавить студента'
    }

    success_url = reverse_lazy('main:index')


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    # fields = ('first_nami', 'last_name', 'avatar', 'is_active',)
    # заменили на
    permission_required = 'main.change_student'
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


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Student
    extra_context = {
        'title': 'Удалить студента'
    }
    success_url = reverse_lazy('main:index')

    def test_func(self):
        """Только суперпользователю доступна кнопка на удаление"""
        return self.request.user.is_superuser


@login_required
@permission_required('main.aktivator_student')
def toggle_activity(request, pk):
    """ Кнопка активации & деактивации студента"""
    student_item = get_object_or_404(Student, pk=pk)
    student_item.is_active = False if student_item.is_active else True

    student_item.save()

    return redirect(reverse('main:index'))
