# Generated by Django 4.0.2 on 2022-02-13 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipdb', '0002_alter_ipdb_sl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipdb',
            name='sl',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
