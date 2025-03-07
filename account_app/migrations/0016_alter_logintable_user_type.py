# Generated by Django 5.1.1 on 2024-10-21 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0015_alter_logintable_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('User', 'user'), ('Rejected', 'rejected'), ('PENDING', 'pending'), ('ADMIN', 'admin'), ('Councellor', 'councellor')], default='pending', max_length=30, null=True),
        ),
    ]
