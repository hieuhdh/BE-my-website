# Generated by Django 4.0.2 on 2022-02-11 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdb',
            name='sl',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]
