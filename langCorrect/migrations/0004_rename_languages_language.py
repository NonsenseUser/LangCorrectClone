# Generated by Django 5.0.3 on 2024-03-29 15:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0003_alter_post_language'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
    ]