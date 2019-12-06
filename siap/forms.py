#from siap.models import MyModel, Problem
""" 
CHOICES = ((1, 1), (2, 2))


class MyForm(forms.ModelForm):
    my_choices = forms.MultipleChoiceField(choices=CHOICES)

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        # maybe you can set initial with self.fields['my_choices'].initial = initial
        # but it doesn't work wity dynamic choices
        obj = kwargs.get('instance')
        if obj:
            initial = [i for i in obj.my_choices.split(',')]
            self.initial['my_choices'] = initial

    def clean_lead_fields(self):
        return ','.join(self.cleaned_data.get('my_choices', []))


class CustomSetForm(forms.ModelForm):
    title = forms.CharField(max_length=32)
    description = forms.CharField(max_length=256)
    duration = forms.CharField(widget=forms.TextInput(attrs= {'min': 20, 'max': 300, 'type': 'number'}))
    problems = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Problem.objects.all()
    ) """
