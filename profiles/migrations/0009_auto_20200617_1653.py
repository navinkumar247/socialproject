# Generated by Django 3.0.3 on 2020-06-17 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_auto_20200617_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='status',
            field=models.CharField(choices=[('accepted', 'accepted'), ('sent', 'sent')], max_length=50),
        ),
    ]
