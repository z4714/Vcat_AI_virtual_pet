# Generated by Django 4.1.2 on 2023-06-15 20:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0006_alter_petsinfo_p_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petsinfo",
            name="uid",
            field=models.IntegerField(default=0),
        ),
    ]