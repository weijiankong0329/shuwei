# Generated by Django 4.2 on 2023-08-06 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_alter_译林_更新时间'),
    ]

    operations = [
        migrations.AlterField(
            model_name='文摘',
            name='图片',
            field=models.ImageField(blank=True, null=True, upload_to='images/wenzhai/'),
        ),
    ]
