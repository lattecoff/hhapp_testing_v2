from django.db import models


# Create your models here.
class Category(models.Model):
    DEV_CATEGORY = (
        ('refrigerator', 'Refrigerator'),
        ('washing_mach', 'Washing Machine')
    )

    name = models.CharField(verbose_name='Category', max_length=50)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name', ]


class Refrigerator(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='Name', max_length=100)
    amount_compressor = models.PositiveSmallIntegerField()
    no_frost = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Refrigerator'
        verbose_name_plural = 'Refrigerators'
        ordering = ['name', 'amount_compressor', 'no_frost', 'category']


class Compressor(models.Model):
    refrigerator = models.ForeignKey(Refrigerator, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(verbose_name='Compressor model', max_length=50)

    class Meta:
        verbose_name = 'Compressor'
        verbose_name_plural = 'Compressors'
        ordering = ['name', ]


class ResearchRef(models.Model):
    RES_STATUS = (
        ('success', 'Success'),
        ('fail', 'Fail'),
        ('in_process', 'In Process')
    )

    device = models.ForeignKey(Refrigerator, on_delete=models.CASCADE, null=True)
    describe = models.TextField(blank=True, null=True, help_text='Additional info, result of research')
    status = models.CharField(max_length=50, choices=RES_STATUS)
    date_start = models.DateField()
    date_finish = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.device} {self.describe} {self.status}'

    class Meta:
        verbose_name = 'Refrigerator research'
        verbose_name_plural = 'Refrigerator research'
        ordering = ['device', 'status', 'date_start', 'date_finish']


