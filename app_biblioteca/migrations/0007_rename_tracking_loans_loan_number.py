# Generated by Django 4.2.6 on 2023-11-29 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0006_loans_tracking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loans',
            old_name='tracking',
            new_name='loan_number',
        ),
    ]