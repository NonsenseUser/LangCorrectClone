# Generated by Django 5.0.3 on 2024-04-01 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('langCorrect', '0010_alter_post_correctionsquantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
                ('commentary', models.TextField(default='')),
                ('isCorrect', models.BooleanField()),
                ('correction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='langCorrect.correction')),
            ],
        ),
    ]
