# Generated by Django 4.1.2 on 2023-06-15 21:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pets", "0008_alter_petsinfo_p_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petsinfo",
            name="p_avatar",
            field=models.TextField(null=True, verbose_name="宠物图像"),
        ),
    ]
