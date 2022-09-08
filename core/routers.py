import logging

logger: logging.Logger = logging.getLogger(__name__)

CARS_SERVICE_APP_LABEL: str = 'cars'

class CarsServiceRouter:
    def db_for_read(self, model, **hints) -> str:
        """
        Reads go to a replica.
        """
        if model._meta.app_label in [CARS_SERVICE_APP_LABEL]:
            print(f"REPLICA DB:  Model: {model} - Hints: {hints} - App label: {model._meta.app_label}")
            return 'users-replica'

    def db_for_write(self, model, **hints) -> str:
        """
        Writes always go to primary.
        """
        
        if model._meta.app_label in [CARS_SERVICE_APP_LABEL]:
            print(f"PRIMARY DB: Model: {model} - Hints: {hints} - App label: {model._meta.app_label}")
            return 'users'

    def allow_relation(self, obj1, obj2, **hints) -> str:
        """
        Relations between objects are allowed if both objects are
        in the primary/replica pool.
        """
        db_set: set[str] = {'users', 'users-replica'}
        if obj1._state.db in db_set and obj2._state.db in db_set:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints) -> str:
        """
        All non-auth models end up in this pool.
        """
        return True
