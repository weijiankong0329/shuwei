# Generated by Django 4.2 on 2023-08-07 01:54

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_文摘_图片'),
    ]

    operations = [
        migrations.AlterField(
            model_name='文摘',
            name='内容',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
