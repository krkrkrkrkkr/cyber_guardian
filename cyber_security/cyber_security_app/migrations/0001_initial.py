# Generated by Django 4.1.3 on 2024-08-09 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SafetyTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q1', models.BooleanField()),
                ('q2', models.BooleanField()),
                ('q3', models.BooleanField()),
                ('q4', models.BooleanField()),
                ('q5', models.BooleanField()),
            ],
        ),
    ]
