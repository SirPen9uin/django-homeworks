from django.db import models
from django.template.defaultfilters import slugify
import datetime


class Phone(models.Model):
    name = models.CharField(max_length=100, default='default_name')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    image = models.CharField(max_length=255, default='default_image.jpg')
    release_date = models.DateField(default=datetime.date.today)
    lte_exists = models.BooleanField(default=False)
    slug = models.SlugField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
