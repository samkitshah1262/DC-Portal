# Generated by Django 4.0.1 on 2022-04-14 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='floated_projects',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='requested_projects',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='user',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
    ]
