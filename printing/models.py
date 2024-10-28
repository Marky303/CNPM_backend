from django.db import models

# Get common database properties
shortLength     = 50  # os.getenv('DATABASE_SHORT_FIELD_LENGTH')
mediumLength    = 255 # os.getenv('DATABASE_MEDIUM_FIELD_LENGTH')
longLength      = 400 # os.getenv('DATABASE_LONG_FIELD_LENGTH')
decimalMaxDigit = 20  # os.getenv('DATABASE_DECIMAL_MAX_DIGIT')
decimalPlace    = 4   # os.getenv('DATABASE_DECIMAL_PLACE')

# Model declaration
class PrinterStatusEnum(models.TextChoices):
    AVAILABLE = 'Available'
    PRINTING = 'Printing'
    MAINTENANCE = 'Maintenance'

class Printer(models.Model):
    # Normal fields
    Name                = models.CharField(max_length=mediumLength, blank=False)         
    SerialNumber        = models.CharField(max_length=shortLength, blank=False)
    ConnectionKey       = models.CharField(max_length=mediumLength, blank=False)
    Location            = models.CharField(max_length=shortLength, blank=False)
    Building            = models.CharField(max_length=shortLength, blank=False)
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
    Date                = models.CharField(max_length=mediumLength, blank=False)         
    PaperType           = models.CharField(max_length=shortLength, blank=False)
    Quantity            = models.PositiveIntegerField(null=False, default=1)
    TotalCost           = models.PositiveIntegerField(null=False, default=0)
    PaperType = models.CharField(
        max_length=shortLength,
        choices=PaperTypeEnum.choices,
        default=PaperTypeEnum.A4,
    )
    
    # Admin page default function
    def __str__(self):
        return str(self.id) + " - " + str(self.TotalCost)
    
    
    

    