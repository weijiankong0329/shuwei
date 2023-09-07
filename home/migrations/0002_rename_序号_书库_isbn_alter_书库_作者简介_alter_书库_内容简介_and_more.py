# Generated by Django 4.2 on 2023-08-29 10:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='书库',
            old_name='序号',
            new_name='ISBN',
        ),
        migrations.AlterField(
            model_name='书库',
            name='作者简介',
            field=ckeditor.fields.RichTextField(blank=True, default='暂无', null=True),
        ),
        migrations.AlterField(
            model_name='书库',
            name='内容简介',
            field=ckeditor.fields.RichTextField(blank=True, default='暂无', null=True),
        ),
        migrations.AlterField(
            model_name='书讯',
            name='定价',
            field=models.CharField(blank=True, default='暂无', max_length=10, null=True),
        ),
    ]
