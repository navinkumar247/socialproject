# Generated by Django 3.0.3 on 2020-06-19 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20200619_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('sent', 'sent'), ('accepted', 'accepted')], max_length=50),
        ),
    ]
