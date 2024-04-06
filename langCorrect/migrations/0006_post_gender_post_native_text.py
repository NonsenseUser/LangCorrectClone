# Generated by Django 5.0.3 on 2024-03-30 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0005_alter_language_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('Мужской', 'Мужской'), ('Женский', 'Женский'), ('Другой', 'Другой'), ('Предпочитаю не указывать', 'Предпочитаю не указывать')], default='Предпочитаю не указывать'),
        ),
        migrations.AddField(
            model_name='post',
            name='native_text',
            field=models.TextField(null=True),
        ),
    ]
