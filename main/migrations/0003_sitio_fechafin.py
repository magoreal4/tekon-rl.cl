# Generated by Django 5.0.1 on 2024-01-18 20:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0002_sitio_empalmee"),
    ]

    operations = [
        migrations.AddField(
            model_name="sitio",
            name="fechaFin",
            field=models.DateField(blank=True, null=True),
        ),
    ]
