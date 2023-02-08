from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=255, verbose_name="Продукт")
    code = models.CharField(max_length=255, verbose_name="Артикул")
    price = models.DecimalField(max_digits=20, decimal_places=2)
    unit = models.CharField(max_length=255, blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} - {self.price}'

    class Meta:
        ordering = ['pk']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'