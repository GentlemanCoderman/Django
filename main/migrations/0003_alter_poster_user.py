# Generated by Django 4.1.7 on 2023-03-10 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_poster'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
    ]
