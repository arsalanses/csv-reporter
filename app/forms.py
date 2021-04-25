from django import forms


class CustomDateTime(forms.DateTimeInput):
    input_type = 'datetime-local'


class RegisterReport(forms.Form):
    start_date = forms.DateTimeField(widget=CustomDateTime)
    end_date = forms.DateTimeField(widget=CustomDateTime)
