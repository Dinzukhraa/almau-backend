# Generated by Django 4.0 on 2024-04-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
