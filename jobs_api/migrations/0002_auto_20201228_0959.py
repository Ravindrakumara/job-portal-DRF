# Generated by Django 3.1.4 on 2020-12-28 04:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='Work_record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('positon', models.CharField(max_length=50)),
                ('workplace', models.CharField(max_length=50)),
                ('start', models.DateField(max_length=65)),
                ('end', models.DateField(max_length=65)),
            ],
            options={
                'verbose_name_plural': 'Work_history',
            },
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name_plural': 'Jobs'},
        ),
        migrations.AddField(
            model_name='jobs',
            name='added_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='experience',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='qualifications',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobs',
            name='reporting_to',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='questionnaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=250)),
                ('answer', models.TextField(max_length=350)),
                ('mark', models.IntegerField()),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs_api.candidates')),
            ],
            options={
                'verbose_name_plural': 'questionnaire',
            },
        ),
        migrations.AddField(
            model_name='candidates',
            name='apply_for',
            field=models.ManyToManyField(related_name='Jobs', to='jobs_api.Jobs'),
        ),
        migrations.AddField(
            model_name='candidates',
            name='work_record',
            field=models.ManyToManyField(related_name='position', to='jobs_api.Work_record'),
        ),
    ]
