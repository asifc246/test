# Generated by Django 3.2.19 on 2023-05-23 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('photo', models.CharField(max_length=300)),
            ],
        ),
    ]
