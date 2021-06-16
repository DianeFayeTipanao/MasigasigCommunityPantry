# Generated by Django 3.1.6 on 2021-06-10 08:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityPantry', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(default='', max_length=75)),
                ('quantity_no', models.PositiveIntegerField(default=0)),
                ('quantity_description', models.CharField(default='', max_length=10)),
                ('date_donated', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='DonatorInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('d_address', models.TextField(blank=True, default='', null=True)),
                ('d_contact', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(99999999999), django.core.validators.MinValueValidator(0)])),
                ('d_email', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='receiverinfo',
            name='r_affiliation',
        ),
        migrations.CreateModel(
            name='ReceiverFeedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[('Very Satisfied', 5), ('Satisfied', 4), ('Neutral', 3), ('Disssatisfied', 2), ('Very Disssatisfied', 1)], default='Neutral')),
                ('comments', models.TextField(blank=True, default='', null=True)),
                ('Suggestions', models.TextField(blank=True, default='', null=True)),
                ('rdetails_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunityPantry.receiverinfo')),
                ('rdetails_ids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunityPantry.receiveddonations')),
            ],
        ),
        migrations.CreateModel(
            name='DonationStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_stock', models.PositiveIntegerField(default=0)),
                ('quantity_description', models.CharField(default='', max_length=10)),
                ('donation_status', models.CharField(choices=[('SPOILED', 'Spoiled'), ('OUT OF STOCK', 'Out of Stock'), ('AVAILABLE', 'Available')], default='AVAILABLE', max_length=12)),
                ('donation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunityPantry.donation')),
            ],
        ),
        migrations.AddField(
            model_name='donation',
            name='donator_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CommunityPantry.donatorinfo'),
        ),
    ]