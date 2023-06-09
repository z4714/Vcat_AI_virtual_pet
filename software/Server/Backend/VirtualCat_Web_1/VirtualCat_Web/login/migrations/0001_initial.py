# Generated by Django 4.1.2 on 2023-06-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "uid",
                    models.IntegerField(
                        default=0,
                        primary_key=True,
                        serialize=False,
                        verbose_name="用户ID",
                    ),
                ),
                (
                    "uname",
                    models.CharField(default="", max_length=30, verbose_name="用户名"),
                ),
            ],
            options={
                "verbose_name": "Account:uid-uname",
                "verbose_name_plural": "用户名",
                "db_table": "account",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="Email",
            fields=[
                (
                    "uid",
                    models.IntegerField(
                        primary_key=True, serialize=False, verbose_name="用户ID"
                    ),
                ),
                ("email", models.EmailField(max_length=30, verbose_name="邮箱")),
            ],
            options={
                "verbose_name": "Email:uid-email",
                "verbose_name_plural": "用户邮箱",
                "db_table": "email",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("uname", models.CharField(max_length=30, verbose_name="用户名")),
                ("pwd", models.CharField(max_length=24, verbose_name="密码")),
                (
                    "nickname",
                    models.CharField(blank=True, max_length=30, verbose_name="昵称"),
                ),
                ("gender", models.BooleanField(null=True, verbose_name="性别")),
                ("birth", models.DateField(null=True, verbose_name="出生日期")),
                ("date", models.DateField(verbose_name="注册日期")),
                (
                    "photo",
                    models.ImageField(null=True, upload_to="", verbose_name="用户头像"),
                ),
            ],
            options={
                "verbose_name": "user infomration : uname",
                "verbose_name_plural": "用户资料",
                "db_table": "user_info",
                "managed": True,
            },
        ),
    ]