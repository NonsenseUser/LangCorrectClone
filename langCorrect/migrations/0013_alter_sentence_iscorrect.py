# Generated by Django 5.0.3 on 2024-04-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0012_remove_correction_corrected_correction_commentary_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sentence',
            name='isCorrect',
            field=models.BooleanField(default=False),
        ),
    ]