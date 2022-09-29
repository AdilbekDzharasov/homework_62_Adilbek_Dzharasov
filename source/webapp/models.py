from django.db import models


class Task(models.Model):
    NEW = "New"

    CHOICES = [
        ('new', 'New'),
        ("in_the_process", 'In the process'),
        ("made", 'Made')
    ]

    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Описание')
    detail_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Детальное описание')
    status = models.CharField(max_length=50, choices=CHOICES, verbose_name='Статус', default=NEW)
    execute_at = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.status} - {self.execute_at}"

