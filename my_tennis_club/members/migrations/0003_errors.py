# Generated by Django 5.0.6 on 2024-07-12 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_journal_alter_clients_uraddress_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
            ],
        ),
    ]
