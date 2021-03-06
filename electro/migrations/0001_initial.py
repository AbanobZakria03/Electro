# Generated by Django 3.0 on 2019-12-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='static/img')),
                ('category', models.CharField(max_length=250)),
                ('name', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('rate', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('password', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=2000)),
                ('telephone', models.IntegerField()),
            ],
        ),
    ]
