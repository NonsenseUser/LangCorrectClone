# Generated by Django 5.0.3 on 2024-03-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0007_remove_language_level_languagelevel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='language',
            name='id',
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
