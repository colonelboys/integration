# Generated by Django 5.0.3 on 2024-03-21 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RendezVous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('description', models.TextField()),
            ],
        ),
    ]
