from django_sharding_library.sharding_functions import BaseShardedModelBucketingStrategy

ZONE_MAP = {
        'zone_1': 'shard_1',
        'zone_2': 'shard_2',
        'zone_3': 'shard_3',
}

class ZoneBasedBucketingStrategy(BaseShardedModelBucketingStrategy):
    """
    A shard selection strategy that assigns shards randomly.
    This is non-deterministic and this strategy assumes the shard is saved to
    the model.
    """
    def __init__(self, shard_group, databases):
        super(ZoneBasedBucketingStrategy, self).__init__(shard_group)
        self.shards = self.get_shards(databases)

    def pick_shard(self, model_sharded_by):
        zone = model_sharded_by.zone
        if zone in ZONE_MAP:
            shard = ZONE_MAP[zone]
            return self.shards[self.shards.index(shard)]
        return self.shards[0]
