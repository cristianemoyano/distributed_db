from django.utils.text import slugify
from django.db import models
from django.contrib.auth.models import User

from django_sharding_library.decorators import model_config
from django_sharding_library.models import TableStrategyModel
from django_sharding_library.fields import TableShardedIDField


@model_config(database='default')
class ShardedMarketIDs(TableStrategyModel):
    pass


@model_config(database='default')
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

    def get_user(self):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=self.user_pk)

    @staticmethod
    def get_user_from_id(user_pk):
        from django.contrib.auth import get_user_model
        return get_user_model().objects.get(pk=user_pk)

    class Meta:
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
