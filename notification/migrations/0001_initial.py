# Generated by Django 4.2.14 on 2024-08-26 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('message', models.CharField(max_length=128)),
                ('notification_type', models.PositiveIntegerField(choices=[(1, 'SMS'), (2, 'EMAIL')], default=2)),
                ('is_sent', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('car_model', models.CharField(max_length=120)),
                ('send_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='alert', to='notification.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='notification', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
