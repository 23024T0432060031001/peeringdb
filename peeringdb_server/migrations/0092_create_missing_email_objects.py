# Generated by Django 3.2.14 on 2022-08-18 11:33

from django.db import migrations, transaction

def forward(apps, schema_editor):

    User = apps.get_model("peeringdb_server", "User")
    EmailAddress = apps.get_model("account", "EmailAddress")

    emails = {}

    for email in EmailAddress.objects.all():
        emails.setdefault(email.user_id, [])
        emails[email.user_id].append(email.email.lower())

    for user in User.objects.exclude(email__isnull=True).exclude(email=""):
        if user.email.lower() not in emails.get(user.id, []):
            if EmailAddress.objects.filter(email=user.email).exists():
                print(
                    f"Could not create missing email address object for user {user.username} - will need to handle manually"
                )
            else:
                EmailAddress.objects.create(email=user.email, user=user, primary=True)


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0091_alter_user_email"),
    ]

    operations = [migrations.RunPython(forward, migrations.RunPython.noop)]
