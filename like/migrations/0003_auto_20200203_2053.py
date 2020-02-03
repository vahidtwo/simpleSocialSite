# Generated by Django 3.0.2 on 2020-02-03 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20200203_0957'),
        ('comment', '0002_auto_20200202_1151'),
        ('like', '0002_auto_20200202_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
