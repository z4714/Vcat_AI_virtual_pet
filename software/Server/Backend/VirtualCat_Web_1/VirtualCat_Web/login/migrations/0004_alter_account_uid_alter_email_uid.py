# Generated by Django 4.1.2 on 2023-06-14 17:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("login", "0003_rename_photo_userinfo_avatar"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="uid",
            field=models.AutoField(
                default=0, primary_key=True, serialize=False, verbose_name="用户ID"
            ),
        ),
        migrations.AlterField(
            model_name="email",
            name="uid",
            field=models.AutoField(
                primary_key=True, serialize=False, verbose_name="用户ID"
            ),
        ),
    ]
