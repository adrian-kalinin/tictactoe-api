# Generated by Django 4.1.6 on 2023-02-07 21:05

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Game",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("board", models.CharField(default="---------", max_length=9)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("RUNNING", "Running"),
                            ("X_WON", "X won"),
                            ("O_WON", "O won"),
                            ("DRAW", "Draw"),
                        ],
                        default="RUNNING",
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
