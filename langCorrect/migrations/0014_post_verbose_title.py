# Generated by Django 5.0.3 on 2024-04-02 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0013_alter_sentence_iscorrect'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='verbose_title',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]
