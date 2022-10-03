from django import forms
from django.forms import inlineformset_factory
from django.urls import reverse

from .models import Care, CareItems


class CareForm(forms.ModelForm):
    id = forms.IntegerField(required=False)

    class Meta:
        model = Care
        fields = ('id', 'doctor', 'patient')

    def __init__(self, *args, **kwargs):
        super(CareForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.disabled = True

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()


class CareItemsForm(forms.ModelForm):
    id = forms.IntegerField()

    class Meta:
        model = CareItems
        fields = ('care', 'id', 'exam', 'is_done')

    def __init__(self, *args, **kwargs):
        super(CareItemsForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['care'].label = ''
        self.fields['care'].widget = forms.HiddenInput()

        self.fields['id'].label = ''
        self.fields['id'].widget = forms.HiddenInput()

        self.fields['exam'].disabled = True

        pk = reverse('exam:care_update_exam', kwargs={'pk': self.instance.pk})
        self.fields['is_done'].widget.attrs['hx-get'] = f'{pk}'
        self.fields['is_done'].widget.attrs['hx-swap'] = f'none'


CareItemsFormset = inlineformset_factory(
    Care,
    CareItems,
    form=CareItemsForm,
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
)
