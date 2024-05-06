# Generated by Django 4.2.11 on 2024-04-16 04:36

import django_peeringdb.fields
import django_peeringdb.models.abstract
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0127_uoar_versioning"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="info_traffic",
            field=models.CharField(
                blank=True,
                choices=[
                    ("", "Not Disclosed"),
                    ("0-20Mbps", "0-20Mbps"),
                    ("20-100Mbps", "20-100Mbps"),
                    ("100-1000Mbps", "100-1000Mbps"),
                    ("1-5Gbps", "1-5Gbps"),
                    ("5-10Gbps", "5-10Gbps"),
                    ("10-20Gbps", "10-20Gbps"),
                    ("20-50Gbps", "20-50Gbps"),
                    ("50-100Gbps", "50-100Gbps"),
                    ("100-200Gbps", "100-200Gbps"),
                    ("200-300Gbps", "200-300Gbps"),
                    ("300-500Gbps", "300-500Gbps"),
                    ("500-1000Gbps", "500-1000Gbps"),
                    ("1-5Tbps", "1-5Tbps"),
                    ("5-10Tbps", "5-10Tbps"),
                    ("10-20Tbps", "10-20Tbps"),
                    ("20-50Tbps", "20-50Tbps"),
                    ("50-100Tbps", "50-100Tbps"),
                    ("100+Tbps", "100+Tbps"),
                ],
                help_text="Total, self-classified traffic in/out to this network.",
                max_length=39,
                verbose_name="Traffic Levels",
            ),
        ),
    ]
