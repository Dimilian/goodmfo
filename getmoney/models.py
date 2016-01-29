from django.db import models

# Create your models here.

class PayVariant(models.Model):


        payvar_name = models.CharField(max_length=100)
        payvar_image = models.ImageField(verbose_name='Изображение', null=True, blank=True)