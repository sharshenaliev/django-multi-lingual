# Generated by Django 4.1.5 on 2023-03-04 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0004_educationcenters_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="educationcenters",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="apps.category"
            ),
        ),
    ]
