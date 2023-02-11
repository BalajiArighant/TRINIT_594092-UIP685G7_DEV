# Generated by Django 4.1.6 on 2023-02-11 11:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="NGO",
            fields=[
                ("ngoID", models.BigAutoField(primary_key=True, serialize=False)),
                ("ngoName", models.CharField(max_length=30)),
                ("username", models.CharField(max_length=45)),
                ("password", models.CharField(max_length=150)),
                ("ngoLocation", models.CharField(max_length=50)),
                ("ngoImpactLocation", models.CharField(max_length=50)),
                ("ngoDesc", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="user",
            fields=[
                ("userID", models.BigAutoField(primary_key=True, serialize=False)),
                ("dob", models.DateField()),
                ("userLocation", models.CharField(max_length=50)),
                ("email", models.EmailField(max_length=100)),
                ("userDesc", models.TextField()),
                (
                    "userl",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Projects",
            fields=[
                ("projectID", models.BigAutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("projDesc", models.TextField()),
                (
                    "ngo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="users.ngo"
                    ),
                ),
                ("user", models.ManyToManyField(to="users.user")),
            ],
        ),
    ]
