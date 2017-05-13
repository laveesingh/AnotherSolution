from django import forms


class CaseForm(forms.Form):
    no_of_tests = forms.CharField(
            widget=forms.TextInput(
                attrs={
                    'id': 'no_of_tests',
                    'class': 'no_class'
                }
            )
        )
    case_type = forms.ChoiceField(
            choices=[
                ('array', 'array'),
                ('string', 'string'),
            ]
        )
