# Generated by Django 4.2.6 on 2023-10-09 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0003_alter_interactions_meeting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactions',
            name='meeting',
            field=models.DateField(default='2023-10-08 '),
        ),
    ]
