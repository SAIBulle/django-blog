# Generated by Django 4.1.2 on 2023-07-19 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0002_sociallink_alter_about_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sociallink',
            old_name='plateform',
            new_name='platform',
        ),
    ]
