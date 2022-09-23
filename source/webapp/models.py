from django.db import models


class Task(models.Model):
    NEW = "Новая"

    CHOICES = [
        (NEW, 'Новая'),
        ("in_the_process", 'В процессе'),
        ("made", 'Сделано')
    ]

    description = models.TextField(max_length=300, null=False, blank=False, verbose_name='Описание')
    detail_description = models.TextField(max_length=3000, null=True, blank=True, verbose_name='Детальное описание')
    status = models.CharField(max_length=50, choices=CHOICES, verbose_name='Статус', default=NEW)
    execute_at = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.status} - {self.execute_at}"

