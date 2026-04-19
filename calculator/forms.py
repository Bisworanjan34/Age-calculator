from django import forms
from .models import Person
from django.core.exceptions import ValidationError
from datetime import date


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"
        widgets = {
            "date_of_birth": forms.DateInput(
                attrs={
                    "type": "date",  # Isse calendar khulega
                    "class": "form-control",  # CSS styling ke liye
                    "max": "2026-12-31",  # Future dates restrict karne ke liye
                }
            ),
            "name": forms.TextInput(
                attrs={"placeholder": "Enter your full name", "class": "form-control"}
            ),
        }

    def clean_date_of_birth(self):
        dob = self.cleaned_data.get("date_of_birth")
        if dob > date.today():
            raise ValidationError("Birth date cannot be in the future!")
        return dob
