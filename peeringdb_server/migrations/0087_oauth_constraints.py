# Generated by Django 3.2.13 on 2022-05-13 16:23

from django.db import connection, migrations, transaction, utils

sql_select_fk_name = "select CONSTRAINT_NAME from INFORMATION_SCHEMA.KEY_COLUMN_USAGE where TABLE_NAME=%s AND REFERENCED_TABLE_NAME='oauth2_provider_application'"


def _fix_constraints(table, cursor):
    cursor.execute(sql_select_fk_name, [table])
    fk_name_row = cursor.fetchall()
    if not fk_name_row:
        return

    fk_name = fk_name_row[0][0]

    sql_drop = f"alter table {table} drop foreign key `{fk_name}`"

    cursor.execute(sql_drop)

    print(sql_drop)

    sql_add = f"alter table {table} add constraint {fk_name} foreign key (`application_id`) REFERENCES `peeringdb_oauth_application` (`id`) ON DELETE CASCADE;"

    print(sql_add)

    cursor.execute(sql_add)


def fix_constraints(apps, schema_editor):
    if schema_editor.connection.vendor != "mysql":
        print("skipping fix_constraints")
        return

    print("fixing constraints")

    with connection.cursor() as cursor:
        cursor.execute("START TRANSACTION;")
        try:
            _fix_constraints("oauth2_provider_grant", cursor)
            _fix_constraints("oauth2_provider_accesstoken", cursor)
            _fix_constraints("oauth2_provider_idtoken", cursor)
            _fix_constraints("oauth2_provider_refreshtoken", cursor)
            cursor.execute("COMMIT;")
        except Exception:
            cursor.execute("ROLLBACK;")
            raise


class Migration(migrations.Migration):
    dependencies = [
        ("peeringdb_server", "0086_auto_20220510_0949"),
    ]

    operations = [migrations.RunPython(fix_constraints, migrations.RunPython.noop)]
