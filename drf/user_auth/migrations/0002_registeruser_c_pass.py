# Generated by Django 3.2.3 on 2021-10-05 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeruser',
            name='c_pass',
            field=models.CharField(default='', max_length=8),
        ),
    ]
