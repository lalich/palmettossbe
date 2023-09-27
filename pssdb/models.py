from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=101)
    school_photo = models.URLField()
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()
    security_description = models.CharField(300)
    

    class Meta:
        verbose_name_plural = 'schools'

class SSS(models.Model):

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    sss_photo = models.URLField()
    years_experience = models.IntegerField()
    description = models.CharField(max_length=300)
    specialty = models.CharField(max_length=101)
    state = models.CharField(max_length=2)
    zip_code = models.IntegerField()

    class Meta:
        verbose_name_plural = 'ssss'