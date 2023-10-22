from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from materials.models import Material


class MaterialCreateView(CreateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy(
        'materials:list')  # это реверс который преобразует нашу джанго запись в урлах ('main:index') и он преобразует когда его вызывают


class MaterialUpdateView(UpdateView):
    model = Material
    fields = ('title', 'body',)
    success_url = reverse_lazy(
        'materials:list')


class MaterialDeleteView(DeleteView):
    model = Material
    success_url = reverse_lazy(
        'materials:list')


class MaterialListView(ListView):
    model = Material


class MaterialDetailView(DetailView):
    model = Material
