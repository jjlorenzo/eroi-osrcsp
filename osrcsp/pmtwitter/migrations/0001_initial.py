
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

  initial = True

  dependencies = [
  ]

  operations = [
    migrations.CreateModel(
      name="Tweet",
      fields=[
        ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
        ("name", models.CharField(max_length=20)),
        ("message", models.CharField(max_length=50)),
        ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
      ],
      options={
        "ordering": ("created_at", "name"),
      },
    ),
  ]
