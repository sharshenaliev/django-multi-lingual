# Generated by Django 4.1.5 on 2023-03-04 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("apps", "0003_alter_advantages_icon_alter_icons_icon"),
    ]

    operations = [
        migrations.AddField(
            model_name="educationcenters",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="apps.category",
            ),
        ),
    ]
