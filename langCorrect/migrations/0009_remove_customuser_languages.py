# Generated by Django 5.0.3 on 2024-03-30 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0008_remove_language_id_alter_language_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='languages',
        ),
    ]
