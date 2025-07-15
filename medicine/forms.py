from django import forms 

class MedForm(forms.Form):
    medicine = forms.CharField(
        label="Medicine Name",
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control", 
            "placeholder": "Enter medicine name (e.g., Aspirin, Vitamin D)",
            "autocomplete": "off"
        })
    )

    stock = forms.IntegerField(
        label="Stock Quantity",
        min_value=0,
        initial=1,
        widget=forms.NumberInput(attrs={
            "class": "form-control", 
            "placeholder": "Enter quantity",
            "min": 0,
            "autocomplete": "off"
        })
    )