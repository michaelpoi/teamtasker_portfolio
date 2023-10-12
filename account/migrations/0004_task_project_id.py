# Generated by Django 4.2.1 on 2023-05-27 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_task_table"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="project_id",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="account.project",
            ),
            preserve_default=False,
        ),
    ]