# Generated by Django 4.1.7 on 2023-08-10 00:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_经训_内容_remove_经训_原文作者_remove_经训_章节_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='章节_经训',
            name='内容',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
