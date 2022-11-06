# Generated by Django 3.2.15 on 2022-11-06 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='market',
            name='delivery_cost',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='delivery_time',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='local_delivery',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='sponsored',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='market',
            name='stars',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
