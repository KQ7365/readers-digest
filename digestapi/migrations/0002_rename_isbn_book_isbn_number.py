# Generated by Django 4.2.7 on 2023-11-10 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('digestapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='isbn',
            new_name='isbn_number',
        ),
    ]
