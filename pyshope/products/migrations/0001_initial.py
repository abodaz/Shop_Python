# Generated by Django 3.0.2 on 2020-01-17 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodcuts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image', models.CharField(max_length=2083)),
            ],
        ),
    ]
