from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Client(models.Model):
    key_client_id = models.AutoField(primary_key=True)
    client_name = models.CharField(max_length=255)
    client_type = models.ForeignKey(ClientType, on_delete=models.SET_NULL, null=True)  # Foreign key to ClientType
    client_location = models.CharField(max_length=255)
    client_state_country = models.CharField(max_length=100)  # Field to represent state/country
    client_contact = models.CharField(max_length=100)
    client_business = models.CharField(max_length=100)
    
    # Contact Information
    primary_contact_email = models.EmailField()
    secondary_contact_email = models.EmailField(blank=True, null=True)
    primary_contact_num = models.CharField(max_length=20)
    secondary_contact_num = models.CharField(max_length=20, blank=True, null=True)
    
    # Contract Details
    date_of_contract = models.DateField()
    expiry_of_contract = models.DateField()
    
    # Additional Information
    status = models.CharField(max_length=50)
    fee_structure = models.CharField(max_length=50)
    time_stamp = models.DateTimeField(auto_now_add=True)  # Automatically set timestamp when created
    
    def __str__(self):
        return self.client_name
