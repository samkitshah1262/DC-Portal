# Generated by Django 4.0.1 on 2022-04-14 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_acceptedstudents_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='acceptedstudents',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='appliedstudents',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]