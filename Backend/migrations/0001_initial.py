# Generated by Django 4.2.6 on 2023-10-08 14:06

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose', models.CharField(choices=[('STATES', 'STATES'), ('MOTORCYCLE', 'MOTORCYCLE')], max_length=30, null=True)),
                ('name', models.CharField(default='Unknown', max_length=40)),
                ('NIP_numer', models.CharField(blank=True, default='Unknown', max_length=10, null=True)),
                ('phone_number', models.CharField(blank=True, default='Unknown', max_length=9, null=True)),
                ('email_address', models.EmailField(blank=True, default='Unknown', max_length=50, null=True)),
                ('price', models.IntegerField(default=0)),
                ('invoice', models.CharField(choices=[('YES', 'YES'), ('NO', 'NO')], max_length=30)),
                ('type', models.CharField(choices=[('LEAD', 'LEAD'), ('CONTACT AGAIN', 'CONTACT AGAIN'), ('DECIDED', 'DECIDED'), ('SUCCESS', 'SUCCESS')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose', models.CharField(choices=[('STATES', 'STATES'), ('MOTORCYCLE', 'MOTORCYCLE')], max_length=30, null=True)),
                ('name', models.CharField(default='Unknown', max_length=40)),
                ('phone_number', models.CharField(blank=True, default='Unknown', max_length=9, null=True)),
                ('price', models.IntegerField(default=0)),
                ('type', models.CharField(choices=[('LEAD', 'LEAD'), ('CONTACT AGAIN', 'CONTACT AGAIN'), ('DECIDED', 'DECIDED'), ('SUCCESS', 'SUCCESS')], max_length=30)),
            ],
            managers=[
                ('managers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose', models.CharField(choices=[('STATES', 'STATES'), ('MOTORCYCLE', 'MOTORCYCLE')], max_length=30, null=True)),
                ('note', models.TextField(default='Max length is 2500 words', max_length=2500)),
            ],
            managers=[
                ('managers', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfEveryone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TypeOfMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Interactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meeting_type', models.CharField(choices=[('SHOWING THE APARTMENT', 'SHOWING THE APARTMENT'), ('VALUATION OF RENOVATION', 'VALUATION OF RENOVATION'), ('CONSTRUCTION INSPECTION', 'CONSTRUCTION INSPECTION'), ('PICKING UP THE MOTORCYCLE', 'PICKING UP THE MOTORCYCLE')], max_length=30)),
                ('meeting', models.DateTimeField()),
                ('note', models.TextField(default='Max length is 1000 words', max_length=1000)),
                ('person_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Backend.contacts')),
                ('person_customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Backend.customers')),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choose', models.CharField(choices=[('STATES', 'STATES'), ('MOTORCYCLE', 'MOTORCYCLE')], max_length=30, null=True)),
                ('describe', models.TextField(default='Max length is 2500 words', max_length=2500)),
                ('customer', models.ManyToManyField(blank=True, to='Backend.customers')),
            ],
            managers=[
                ('managers', django.db.models.manager.Manager()),
            ],
        ),
    ]
