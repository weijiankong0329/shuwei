# Generated by Django 4.1.7 on 2023-08-07 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_评论_观点_通过'),
    ]

    operations = [
        migrations.AlterField(
            model_name='文艺',
            name='作者',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='文艺',
            name='图片',
            field=models.ImageField(blank=True, null=True, upload_to='images/wenyi/'),
        ),
        migrations.AlterField(
            model_name='评论_文艺',
            name='通过',
            field=models.CharField(default='审查中', max_length=100),
        ),
    ]
