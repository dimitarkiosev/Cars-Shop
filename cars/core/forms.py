from django import forms
from cars.core.models import CarComment


class CarCommentForm(forms.ModelForm):
    class Meta:
        model= CarComment
        fields = ['text']
        labels = {
            'text': '',
        }
        widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Add comment here...','rows': 3}),
        }


class SearchCarForm(forms.Form):
    car_name = forms.CharField(
        max_length=50,
        required=False,
        label='',
        widget=forms.TextInput(attrs={'placeholder': 'Search car'}),
    )