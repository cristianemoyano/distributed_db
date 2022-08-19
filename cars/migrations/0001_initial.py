# Generated by Django 3.2.15 on 2022-08-19 16:44

from django.db import migrations, models
import django_sharding_library.fields
import django_sharding_library.id_generation_strategies


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', django_sharding_library.fields.TableShardedIDField(primary_key=True, serialize=False, source_table_name='cars.ShardedCarIDs', strategy=django_sharding_library.id_generation_strategies.TableStrategy(backing_model_name='cars.ShardedCarIDs'))),
                ('name', models.CharField(max_length=50, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('company', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Car',
                'verbose_name_plural': 'Cars',
            },
        ),
        migrations.CreateModel(
            name='ShardedCarIDs',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('stub', models.NullBooleanField(default=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
