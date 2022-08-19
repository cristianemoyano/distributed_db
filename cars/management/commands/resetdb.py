from django.core.management.base import BaseCommand, CommandError
from django.db import connections


class Command(BaseCommand):
    help = 'Reset POSTGRES DB'

    def handle(self, *args, **options):
        try:
            with connections['shard_1'].cursor() as cursor:
                cursor.execute("DROP SCHEMA public CASCADE;")
                cursor.execute("CREATE SCHEMA public;")
            with connections['shard_2'].cursor() as cursor:
                cursor.execute("DROP SCHEMA public CASCADE;")
                cursor.execute("CREATE SCHEMA public;")
            with connections['shard_3'].cursor() as cursor:
                cursor.execute("DROP SCHEMA public CASCADE;")
                cursor.execute("CREATE SCHEMA public;")
            with connections['users'].cursor() as cursor:
                cursor.execute("DROP SCHEMA public CASCADE;")
                cursor.execute("CREATE SCHEMA public;")

        except Exception as exc:
            raise CommandError(str(exc))
        
        self.stdout.write(self.style.SUCCESS('Successfully db reseted.'))

