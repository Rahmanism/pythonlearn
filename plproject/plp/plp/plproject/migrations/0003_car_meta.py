# Generated by Django 2.1.7 on 2019-03-12 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plproject', '0002_auto_20190309_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='meta',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
