# Generated by Django 5.1.3 on 2024-11-22 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_session_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='availability',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='specialization',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='status',
            field=models.CharField(choices=[('upcoming', 'Upcoming'), ('completed', 'Completed')], default='upcoming', max_length=20),
        ),
    ]
