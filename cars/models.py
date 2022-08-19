from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser

from django_sharding_library.decorators import shard_storage_config, model_config
from django_sharding_library.models import ShardedByMixin, TableStrategyModel
from django_sharding_library.fields import TableShardedIDField


@shard_storage_config('postgres')
class User(AbstractUser, ShardedByMixin):
    pass


@model_config(database='default')
class ShardedCarIDs(TableStrategyModel):
    pass


@model_config(database='default')
class Car(models.Model):
    id = TableShardedIDField(primary_key=True, source_table_name='cars.ShardedCarIDs')
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(null=True, blank=True)
    company = models.CharField(max_length=120)

    def get_shard(self):
        return self.company.user.shard

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.name)

            has_slug = Car.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count) 
                has_slug = Car.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)
