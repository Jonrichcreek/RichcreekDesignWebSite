# Generated by Django 2.2.1 on 2019-06-07 18:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pic_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('pic_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pic_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pic_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('pic_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('blurb', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('publish', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
