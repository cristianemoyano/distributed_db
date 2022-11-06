from django.contrib import admin
from markets.models import Market, ShardedMarketIDs, User

class MarketAdmin(admin.ModelAdmin):
    using = 'shard_1'

    def get_queryset(self, request):
        zone = request.GET.get('e', '1')
        ZONE_MAP = {
            '1': 'shard_1',
            '2': 'shard_2',
            '3': 'shard_3',
        }
        # Tell Django to look for objects on the 'other' database.
        return super().get_queryset(request).using(ZONE_MAP[zone])

class ShardedMarketIDsAdmin(admin.ModelAdmin):
    using = 'default'


class UserAdmin(admin.ModelAdmin):
    using = 'default'

admin.site.register(Market, MarketAdmin)
admin.site.register(ShardedMarketIDs, ShardedMarketIDsAdmin)
admin.site.register(User, UserAdmin)
