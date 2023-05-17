# Generated by Django 4.1 on 2023-05-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_contributions'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='categories',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
