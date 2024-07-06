
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import FirmDetails
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class FirmDetailsForm(forms.ModelForm):
    class Meta:
        model = FirmDetails
        fields = [
            'firm_name', 'mobile_no', 'address', 'gstn_no', 'msme_status', 
            'certification_name', 'firm_pdf', 'pan', 'manf_plant_location', 
            'manf_capacity', 'gcv_range', 'moisture', 'fire', 'base_material_used', 
            'material_source', 'material_price', 'binding_material', 'untied_capacity',
            'No_of_loi', 'pref_plant_of_unl', 'dist_from_plant', 'Trans_Charge',
            'Future_cap_add', 'plant_location', 'capacity', 'GCV', 'raw_material',
        ]
        widgets = {
            'address': forms.Textarea(attrs={
                'rows': 1,
                'cols': 70,
                'placeholder': 'Enter binding material details',
            }),
            'msme_status': forms.CheckboxInput(),
            'fire': forms.NumberInput(attrs={
                'placeholder': 'Enter in percentage',
                'step': '0.01',
                'min': '0',
                'max': '100',
            }),
            'material_price': forms.NumberInput(attrs={
                'placeholder': 'Enter the material price',
                'step': '0.01',
            }),
            'binding_material': forms.Textarea(attrs={
                'rows': 1,
                'cols': 40,
                'placeholder': 'Enter binding material details',
            }),
            'plant_location': forms.Textarea(attrs={
                'rows': 1,  # Adjusted to allow multiple lines
                'cols': 40,
                'placeholder': 'Enter plant location details',
            }),
            'Future_cap_add': forms.CheckboxInput(),
        }


    def clean_firm_pdf(self):
        firm_pdf = self.cleaned_data.get('firm_pdf', False)
        if not firm_pdf:
            raise forms.ValidationError("Please upload your firm PDF.")
        return firm_pdf

    def clean(self):
        cleaned_data = super().clean()
        msme_status = cleaned_data.get("msme_status")
        certification_name = cleaned_data.get("certification_name")

        if msme_status and not certification_name:
            self.add_error('certification_name', "This field is required if MSME status is Yes.")

        Future_cap_add = cleaned_data.get('Future_cap_add')

        if Future_cap_add:
            plant_location = cleaned_data.get('plant_location')
            capacity = cleaned_data.get('capacity')
            gcv = cleaned_data.get('GCV')
            raw_material = cleaned_data.get('raw_material')

            if not plant_location:
                self.add_error('plant_location', "Plant location is required.")
            if not capacity:
                self.add_error('capacity', "Capacity is required.")
            if not gcv:
                self.add_error('GCV', "GCV is required.")
            if not raw_material:
                self.add_error('raw_material', "Raw material details are required.")
        else:
            # Ensure these fields are not marked as required when Future_cap_add is False
            cleaned_data['plant_location'] = ""
            cleaned_data['capacity'] = ""
            cleaned_data['GCV'] = ""
            cleaned_data['raw_material'] = ""

        return cleaned_data