# Generated by Django 3.2.4 on 2021-06-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fruityapi', '0005_alter_fruity_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fruity',
            name='type',
            field=models.CharField(max_length=25),
        ),
    ]
