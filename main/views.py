from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from main.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'main/index.html'


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
    template_name = 'main/student_detail.html'

# def view_student(request, pk):
#     """Просмотр одного студента"""
#     students_item = get_object_or_404(Student, pk=pk)
#     context = {
#         'object': students_item,
#         'title': 'Студент'
#     }
#     return render(request, 'main/student_detail.html', context)
