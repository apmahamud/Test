# Generated by Django 5.0.3 on 2024-03-25 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_cdr_created_alter_cdr_call_duration_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cdr',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
