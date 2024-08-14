from django import forms
from .models import Subject

class SubjectModelForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ["name","topics","start_date"]
        widgets = {
            "name":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "topics":forms.TextInput(attrs={"class":"form-control mb-3"}),
            "start_date":forms.DateInput(attrs={'type':'date',"class":"form-control mb-3"}),
        }