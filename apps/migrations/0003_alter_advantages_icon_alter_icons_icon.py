# Generated by Django 4.1.5 on 2023-03-04 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0002_alter_contacts_phone"),
    ]

    operations = [
        migrations.AlterField(
            model_name="advantages",
            name="icon",
            field=models.FileField(upload_to="images/icons"),
        ),
        migrations.AlterField(
            model_name="icons",
            name="icon",
            field=models.FileField(upload_to="images/icons"),
        ),
    ]
