# Generated by Django 3.1.6 on 2021-06-23 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CommunityPantry', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receiveddonations',
            name='received_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='CommunityPantry.receiverinfo'),
        ),
    ]
