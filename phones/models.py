from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
   objects = None
   id = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=50)
   image = models.CharField(max_length=200)
   price = models.DecimalField(max_digits=20, decimal_places=1)
   release_date = models.DateField(auto_now=False)
   lte_exists = models.BooleanField(blank=False)
   slug = models.SlugField(unique=True, blank=True)


   def save(self, *args, **kwargs):
      """Для автоматической генерации значения поля slug на основе значения поля name"""
      if not self.slug:
         self.slug = slugify(self.name)
         super().save(*args, **kwargs)

