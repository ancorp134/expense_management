# Generated by Django 3.2.22 on 2023-10-12 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20231012_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advancetripplan',
            name='month',
            field=models.CharField(choices=[('January', 'January'), ('February', 'February'), ('March', 'March'), ('April', 'April'), ('May', 'May'), ('June', 'June'), ('July', 'July'), ('August', 'August'), ('September', 'September'), ('October', 'October'), ('November', 'November'), ('December', 'December')], default='January', max_length=10),
        ),
    ]