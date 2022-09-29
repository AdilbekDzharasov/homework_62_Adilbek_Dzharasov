# Generated by Django 4.1.1 on 2022-09-29 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_task_detail_description_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('new', 'New'), ('in_the_process', 'In the process'), ('made', 'Made')], default='New', max_length=50, verbose_name='Статус'),
        ),
    ]
