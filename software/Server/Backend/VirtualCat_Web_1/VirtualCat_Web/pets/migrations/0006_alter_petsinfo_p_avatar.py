# Generated by Django 4.1.2 on 2023-06-15 19:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0005_alter_petsinfo_p_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petsinfo",
            name="p_avatar",
            field=models.FileField(null=True, upload_to="", verbose_name="宠物图像"),
        ),
    ]