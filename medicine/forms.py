from django import forms 

class MedForm(forms.Form):
    medicine = forms.CharField(
        label="Enter ",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Arnica"})
    )

    stock = forms.IntegerField(
            label="Stock",
            min_value=0,
            widget=forms.NumberInput(attrs={"class": "form-control","placeholder": "1","min": 0
            })
        )