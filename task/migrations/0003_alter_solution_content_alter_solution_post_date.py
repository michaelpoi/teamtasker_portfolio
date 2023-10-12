# Generated by Django 4.2.1 on 2023-06-04 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("task", "0002_alter_solution_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="solution",
            name="content",
            field=models.FileField(default=None, upload_to="uploads/"),
        ),
        migrations.AlterField(
            model_name="solution",
            name="post_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]