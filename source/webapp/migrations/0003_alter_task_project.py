# Generated by Django 4.1.1 on 2022-10-14 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_project_task_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, related_name='tasks', to='webapp.project', verbose_name='Project'),
            preserve_default=False,
        ),
    ]