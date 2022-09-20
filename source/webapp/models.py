from django.db import models


class Task(models.Model):
    NEW = "NEW"
    IN_THE_PROCESS = "IN_THE_PROCESS"
    MADE = "MADE"

    CHOICES = [
        (NEW, 'Новая'),
        (IN_THE_PROCESS, 'В процессе'),
        (MADE, 'Сделано')
    ]

    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.CharField(max_length=50, choices=CHOICES, verbose_name='Статус', default=NEW)
    execute_at = models.DateField(verbose_name='Дата выполнения', null=True, blank=True)

    def __str__(self):
        return f"{self.description} - {self.status} - {self.execute_at}"

