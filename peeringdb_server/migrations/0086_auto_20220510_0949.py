# Generated by Django 3.2.13 on 2022-05-10 09:49

import django.core.validators
import django_inet.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0085_org_oauth"),
    ]

    operations = [
        migrations.AlterField(
            model_name="commandlinetool",
            name="tool",
            field=models.CharField(
                choices=[
                    ("pdb_renumber_lans", "Renumber IP Space"),
                    ("pdb_fac_merge", "Merge Facilities"),
                    ("pdb_fac_merge_undo", "Merge Facilities: UNDO"),
                    ("pdb_undelete", "Restore Object(s)"),
                    ("pdb_validate_data", "Validate Data"),
                    ("pdb_ixf_ixp_member_import", "IX-F Import"),
                ],
                help_text="name of the tool",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="ixfmemberdata",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="ixlan",
            name="rs_asn",
            field=django_inet.models.ASNField(
                blank=True,
                default=0,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Route Server ASN",
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="asn",
            field=django_inet.models.ASNField(
                unique=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkfacility",
            name="local_asn",
            field=django_inet.models.ASNField(
                blank=True,
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="Local ASN",
            ),
        ),
        migrations.AlterField(
            model_name="networkixlan",
            name="asn",
            field=django_inet.models.ASNField(
                validators=[django.core.validators.MinValueValidator(0)],
                verbose_name="ASN",
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="flagged",
            field=models.BooleanField(
                blank=True, help_text="Flag the organization for deletion", null=True
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="flagged_date",
            field=models.DateTimeField(
                blank=True,
                help_text="Date when the organization was flagged",
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="organization",
            name="logo",
            field=models.FileField(
                blank=True,
                help_text="Allows you to upload and set a logo image file for this organization",
                null=True,
                upload_to="logos_user_supplied/",
            ),
        ),
        migrations.AlterField(
            model_name="userorgaffiliationrequest",
            name="asn",
            field=django_inet.models.ASNField(
                blank=True,
                help_text="The ASN entered by the user",
                null=True,
                validators=[django.core.validators.MinValueValidator(0)],
            ),
        ),
    ]
