# Generated by Django 3.1.4 on 2020-12-28 04:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_api', '0003_auto_20201228_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidates',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='candidates',
            name='apply_for',
            field=models.ManyToManyField(related_name='Jobs', to='jobs_api.Jobs'),
        ),
    ]
