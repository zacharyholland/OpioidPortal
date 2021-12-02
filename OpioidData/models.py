from django.db import models
from django.db.models.fields import NOT_PROVIDED, BooleanField

# Create your models here.
class Prescriber(models.Model) :
    npi = models.CharField(max_length=10)
    Fname = models.CharField(max_length=30)
    Lname = models.CharField(max_length=30)
    Gender = models.CharField(max_length=7)
    State = models.CharField(max_length=2)

    class Meta:
        db_table = "pd_prescriber"

    @property
    def full_name(self):
            return '%s %s' % (self.Fname, self.Lname)

    def __str__(self):
        return (self.full_name)

class Drug(models.Model) :
    drugname = models.CharField(max_length=100)
    isopioid = models.BooleanField(default=False)

    class Meta:
        db_table = "pd_drugs"

    def __str__(self) :
        return (self.drugname)