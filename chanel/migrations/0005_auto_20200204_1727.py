# Generated by Django 3.0.2 on 2020-02-04 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chanel', '0004_chanel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chanel',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
