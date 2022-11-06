from django.contrib import admin
from django.utils.translation import gettext_lazy
from markets.models import Market, ShardedMarketIDs, User

class MarketAdminShard1(admin.ModelAdmin):
    using = 'shard_1'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

class MarketAdminShard2(admin.ModelAdmin):
    using = 'shard_2'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

class MarketAdminShard3(admin.ModelAdmin):
    using = 'shard_3'

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

class ShardedMarketIDsAdmin(admin.ModelAdmin):
    using = 'default'


class UserAdmin(admin.ModelAdmin):
    using = 'default'

# SHARD 1
class AdminShard1(admin.AdminSite):
    index_title = gettext_lazy('Shard 1')
admin_shard1 = AdminShard1('admin-shard1')
admin_shard1.register(Market, MarketAdminShard1)
admin_shard1.register(ShardedMarketIDs, ShardedMarketIDsAdmin)
admin_shard1.register(User, UserAdmin)

# SHARD 2
class AdminShard2(admin.AdminSite):
    index_title = gettext_lazy('Shard 2')
    index_template = 'admin/index.html'

admin_shard2 = AdminShard2('admin-shard2')
admin_shard2.register(Market, MarketAdminShard2)
admin_shard2.register(ShardedMarketIDs, ShardedMarketIDsAdmin)
admin_shard2.register(User, UserAdmin)

# SHARD 3
class AdminShard3(admin.AdminSite):
    index_title = gettext_lazy('Shard 3')
admin_shard3 = AdminShard3('admin-shard3')
admin_shard3.register(Market, MarketAdminShard3)
admin_shard3.register(ShardedMarketIDs, ShardedMarketIDsAdmin)
admin_shard3.register(User, UserAdmin)
