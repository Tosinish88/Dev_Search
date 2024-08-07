# Generated by Django 5.0.7 on 2024-07-16 09:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_alter_project_description_and_more"),
        ("users", "0002_profile_username"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="owner",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="users.profile",
            ),
        ),
    ]
