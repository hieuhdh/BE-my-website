# Generated by Django 4.0.2 on 2022-02-11 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ipdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField(blank=True, null=True)),
                ('post', models.TextField(blank=True, null=True)),
                ('sl', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Iphomedb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.TextField(blank=True, null=True)),
                ('sl', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]