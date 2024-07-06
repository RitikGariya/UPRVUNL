from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class FirmDetails(models.Model):
    firm_name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=15)
    address = models.TextField()
    gstn_no = models.CharField(max_length=15)
    msme_status = models.BooleanField(default=False)
    certification_name = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=100)
    manf_plant_location = models.CharField(max_length=30)
    manf_capacity = models.CharField(max_length=30)
    gcv_range = models.CharField(max_length=30)
    moisture = models.CharField(max_length=30)
    fire = models.DecimalField(
        null=True,
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        help_text="Enter a percentage, till 2 decimal places"
    )
    base_material_used = models.CharField(max_length=30)
    material_source = models.CharField(max_length=30)
    material_price = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Enter the material price, till 2 decimal places"
    )
    binding_material = models.TextField()
    untied_capacity = models.CharField(max_length=30)
    No_of_loi = models.CharField(max_length=30)
    pref_plant_of_unl = models.CharField(max_length=30)
    dist_from_plant = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Enter Distance From Plant, till 2 decimal places"
    )
    Trans_Charge = models.DecimalField(
        null=True,
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        help_text="Transportation charger in Rs/Trans, till 2 decimal places."
    )
    Future_cap_add = models.BooleanField(default=False)
    plant_location = models.TextField()
    capacity = models.CharField(max_length=30)
    GCV = models.CharField(max_length=30)
    raw_material = models.CharField(max_length=30)
    firm_pdf = models.FileField(upload_to="pdf/")

    def __str__(self):
        return self.firm_name
