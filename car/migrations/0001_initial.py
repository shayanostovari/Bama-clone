# Generated by Django 4.2.14 on 2024-08-16 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('modified_time', models.DateTimeField(auto_now_add=True)),
                ('body', models.SmallIntegerField(choices=[('1', '1piece'), ('2', '2piece'), ('3', 'Multiple_piece'), ('4', 'whole_color')], null=True)),
                ('title', models.CharField(max_length=60)),
                ('tip', models.CharField(blank=True, null=True)),
                ('color', models.CharField()),
                ('model_year', models.SmallIntegerField()),
                ('description', models.TextField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
