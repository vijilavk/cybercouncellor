# Generated by Django 5.1.1 on 2024-09-13 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Councellor',
            new_name='Councellortable',
        ),
        migrations.AlterField(
            model_name='logintable',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('DEACTIVE', 'Deactive')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='logintable',
            name='user_type',
            field=models.CharField(choices=[('ADMIN', 'admin'), ('Councellor', 'councellor')], max_length=30, null=True),
        ),
    ]
