from django import forms
from django.core.exceptions import ValidationError

from goodmfo.models import UserInfo


class PersonalDataForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = [
            'surname',
            'name',
            'patronymic',
            'email',
            'phone',
            'homephone',
            'birth',
        ]

    birth = forms.DateField(
        widget=forms.DateInput(format='%d.%m.%Y'),
        input_formats=('%d.%m.%Y', ),
    )

    def clean_surname(self):
        surname = self.cleaned_data['surname']

        if surname == 'dd':
            raise ValidationError('ERROR')
        return surname
