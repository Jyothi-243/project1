# Generated by Django 4.2.2 on 2023-08-07 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('experience', models.IntegerField()),
                ('subject', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
    ]
