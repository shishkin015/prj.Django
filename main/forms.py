from django import forms

from main.models import Student, Subject


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        # fields = '__all__'  # все поля для редактирования
        fields = ('first_nami', 'last_name', 'email')  # определенные поля для редактирования
        # exclude = ('is_active',)  # исключить поле из редактирования
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'title'}),
        }

    def clean_email(self):
        clean_data = self.cleaned_data['email']

        if 'sky.pro' not in clean_data:
            raise forms.ValidationError('Почта не относится к учебному заведению')

        return clean_data


class SubjectForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'
