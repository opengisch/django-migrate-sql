from django.db import migrations

import migrate_sql.operations


class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrate_sql.operations.CreateSQL(
            name="sale",
            sql="CREATE TYPE sale AS (arg1 int); -- 1",
            reverse_sql="DROP TYPE sale",
        ),
    ]
