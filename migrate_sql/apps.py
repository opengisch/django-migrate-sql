from django.apps import AppConfig
from django.core.management.commands import makemigrations

from migrate_sql.autodetector import MigrationAutodetectorMixin


def patch_autodetector():
    if not issubclass(makemigrations.MigrationAutodetector, MigrationAutodetectorMixin):
        makemigrations.MigrationAutodetector = type(
            "MigrationAutodetector",
            (
                MigrationAutodetectorMixin,
                makemigrations.MigrationAutodetector,
            ),
            {},
        )


class MigrateSQLConfig(AppConfig):
    name = "migrate_sql"

    def ready(self):
        patch_autodetector()
