# Generated by Django 5.1.1 on 2024-10-17 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0013_alter_logintable_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('Rejected', 'rejected'), ('ADMIN', 'admin'), ('Councellor', 'councellor'), ('PENDING', 'pending'), ('User', 'user')], default='pending', max_length=30, null=True),
        ),
    ]
