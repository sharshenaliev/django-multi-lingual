# Generated by Django 4.1.5 on 2023-03-04 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0005_alter_educationcenters_category"),
    ]

    operations = [
        migrations.RenameField(
            model_name="educationcenters",
            old_name="spezialization",
            new_name="specialization",
        ),
    ]
