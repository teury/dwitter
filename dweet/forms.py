from django import forms
from dweet.models import Dweety

class DweetForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput,required=False)
    class Meta:
        model = Dweety
        fields = ('id','value', 'user')