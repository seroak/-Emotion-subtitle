# Generated by Django 4.1 on 2023-02-05 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_img",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
