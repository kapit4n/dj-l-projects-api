# Generated by Django 4.1 on 2023-05-17 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_skills_alter_project_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='size',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]