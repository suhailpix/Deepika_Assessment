# Generated by Django 4.2.11 on 2024-03-22 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ExpenseTrackerApp', '0009_userdb_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='expense',
            name='login_password',
        ),
    ]
