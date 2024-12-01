from django.db import models
from account.models import *

# Get common database properties
shortLength     = 50  # os.getenv('DATABASE_SHORT_FIELD_LENGTH')
mediumLength    = 255 # os.getenv('DATABASE_MEDIUM_FIELD_LENGTH')
longLength      = 400 # os.getenv('DATABASE_LONG_FIELD_LENGTH')
decimalMaxDigit = 20  # os.getenv('DATABASE_DECIMAL_MAX_DIGIT')
decimalPlace    = 4   # os.getenv('DATABASE_DECIMAL_PLACE')

# Model declaration
class PrinterStatusEnum(models.TextChoices):
    AVAILABLE = 'Available'
    MAINTENANCE = 'Maintenance'

class Printer(models.Model):
    # Normal fields
    Name                = models.CharField(max_length=mediumLength, blank=False)         
    SerialNumber        = models.CharField(max_length=shortLength, blank=False)
    Brand               = models.CharField(max_length=mediumLength, blank=False)
    Location            = models.CharField(max_length=shortLength, blank=False)
    Model               = models.CharField(max_length=shortLength, blank=False)
    Status = models.CharField(
        max_length=shortLength,
        choices=PrinterStatusEnum.choices,
        default=PrinterStatusEnum.AVAILABLE,
    )
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + ". " + self.Name
    
class PaperTypeEnum(models.TextChoices):
    A2 = 'A2'
    A3 = 'A3'
    A4 = 'A4'
    
class History(models.Model):
    # Normal fields
    Date                = models.CharField(max_length=mediumLength, blank=True, null=True)
    Location            = models.CharField(max_length=shortLength, blank=True, null=True)
    Direction           = models.CharField(max_length=shortLength, blank=True, null=True)
    FileName            = models.CharField(max_length=longLength, blank=True, null=True)
    Pages               = models.PositiveIntegerField(null=False, default=1)       
    Copies              = models.PositiveIntegerField(null=False, default=1)   
    Cost                = models.PositiveIntegerField(null=False, default=1)
    FileType            = models.CharField(max_length=shortLength, blank=True, null=True)
    Size = models.CharField(
        max_length=shortLength,
        choices=PaperTypeEnum.choices,
        default=PaperTypeEnum.A4,
    )
    
    # Foreignkey field
    Printer             = models.ForeignKey(Printer, on_delete=models.SET_NULL, null=True)
    User                = models.ForeignKey(UserAccount, on_delete=models.SET_NULL, null=True)
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + " - " + str(self.TotalCost)
    
class Setting(models.Model):
    # Normal fields
    AllowedFiles        = models.CharField(max_length=mediumLength, blank=True, null=True)
    Token               = models.PositiveIntegerField(null=False, default=1)
    Time                = models.CharField(max_length=mediumLength, blank=True, null=True)
    
    
    

    