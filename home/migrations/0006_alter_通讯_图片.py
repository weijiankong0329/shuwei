# Generated by Django 4.1.7 on 2023-08-01 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_发布时间_通讯_更新时间_rename_回答_问答_答案_通讯_发布状态'),
    ]

    operations = [
        migrations.AlterField(
            model_name='通讯',
            name='图片',
            field=models.ImageField(default='null', null=True, upload_to='images/通讯/'),
        ),
    ]
