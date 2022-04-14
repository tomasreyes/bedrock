# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

# Generated by Django 3.2.12 on 2022-04-04 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("mozorg", "0001_squashed_0004_squash"),
    ]

    operations = [
        migrations.CreateModel(
            name="WebvisionDoc",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("content", models.JSONField()),
            ],
        ),
    ]
