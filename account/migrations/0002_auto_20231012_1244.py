# Generated by Django 3.2.22 on 2023-10-12 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advancetripplan',
            name='month',
            field=models.CharField(default='January', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='advancetripplan',
            name='year',
            field=models.CharField(default='2023', max_length=20, null=True),
        ),
    ]