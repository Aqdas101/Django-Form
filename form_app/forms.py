from django import forms
from .models import Client, ClientType


class ClientForm(forms.ModelForm):
    new_client_type = forms.CharField(max_length=100, required=False, label="New Client Type")

    class Meta:
        model = Client
        fields = [
            'client_name', 
            'client_type', 
            'client_location', 
            'client_state_country', 
            'client_contact',
            'client_business', 
            'primary_contact_email', 
            'secondary_contact_email',
            'primary_contact_num', 
            'secondary_contact_num', 
            'date_of_contract', 
            'expiry_of_contract',
            'status', 
            'fee_structure'
        ]

         # Custom widgets for the date fields to render them as date pickers
        widgets = {
            'date_of_contract': forms.DateInput(attrs={'type': 'date'}),
            'expiry_of_contract': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        self.fields['client_type'].queryset = ClientType.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        new_client_type = cleaned_data.get("new_client_type")

        if new_client_type:
            client_type, created = ClientType.objects.get_or_create(name=new_client_type)
            cleaned_data['client_type'] = client_type

        return cleaned_data




