from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

from django_sharding_library.decorators import model_config, shard_storage_config
from django_sharding_library.models import TableStrategyModel, ShardedByMixin
from django_sharding_library.fields import TableShardedIDField


# A model for use with a sharded model to generate pk's using
# an autoincrement field on the backing TableStrategyModel.
@model_config(database='default')
class ShardedMarketIDs(TableStrategyModel):
    pass

# An implementation of the extension of a the Django user to add
# the mixin provided in order to save the shard on the user.
@shard_storage_config(shard_group='markets')
class User(AbstractUser, ShardedByMixin):
    ZONE_1 = 'zone_1'
    ZONE_2 = 'zone_2'
    ZONE_3 = 'zone_3'
    ZONE_CHOICES = [
        (ZONE_1, 'Zona 1'),
        (ZONE_2, 'Zona 2'),
        (ZONE_3, 'Zona 3'),
    ]
    # Patch for Django 1.11
    groups = None
    user_permissions = None
    zone = models.CharField(
        max_length=120,
        choices=ZONE_CHOICES,
        default=ZONE_1,
        null=True,
        blank=True,
    )


@model_config(shard_group='markets')
class Market(models.Model):
    id = TableShardedIDField(primary_key=True, source_table_name='markets.ShardedMarketIDs')
    name = models.CharField(max_length=50,null=True)
    slug = models.SlugField(null=True, blank=True)
    address = models.CharField(max_length=120)

    sponsored = models.BooleanField(null=True, blank=True)
    local_delivery = models.BooleanField(null=True, blank=True)
    delivery_time = models.CharField(max_length=120, null=True, blank=True)
    delivery_cost = models.PositiveIntegerField(null=True, blank=True)
    stars = models.CharField(max_length=3, null=True, blank=True)

    user_pk = models.PositiveIntegerField()

    def get_shard(self):
        return User.objects.get(pk=self.user_pk).shard

    @property
    def zone(self):
        return User.objects.get(pk=self.user_pk).zone

    @property
    def shard(self):
        return User.objects.get(pk=self.user_pk).shard

    @staticmethod
    def get_shard_from_id(user_pk):
        return User.objects.get(pk=user_pk).shard

    def get_user(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.user_pk)

    @staticmethod
    def get_user_from_id(user_pk):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=user_pk)

    class Meta:
        app_label = 'markets'
        verbose_name = 'Market'
        verbose_name_plural = 'Markets'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == None:
            slug = slugify(self.name)

            has_slug = Market.objects.filter(slug=slug).exists()
            count = 1
            while has_slug:
                count += 1
                slug = slugify(self.name) + '-' + str(count) 
                has_slug = Market.objects.filter(slug=slug).exists()

            self.slug = slug
        super().save(*args, **kwargs)
