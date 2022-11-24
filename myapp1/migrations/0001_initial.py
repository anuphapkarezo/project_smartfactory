# Generated by Django 4.1.1 on 2022-11-24 09:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company_contact_name_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=10)),
                ('contact_firstname', models.CharField(default='', max_length=100)),
                ('contact_lastname', models.CharField(default='', max_length=100)),
                ('contact_email', models.CharField(default='', max_length=50)),
                ('contact_phone', models.CharField(default='', max_length=20)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company_master_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_code', models.CharField(max_length=10, unique=True)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product_master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, unique=True)),
                ('category_name', models.CharField(default='', max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_daily_transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_take_off', models.CharField(default='', max_length=20)),
                ('factory_name', models.CharField(default='', max_length=5)),
                ('waste_item_code', models.CharField(default='', max_length=9)),
                ('waste_group_code', models.CharField(default='', max_length=5)),
                ('detail_no', models.CharField(default='', max_length=20)),
                ('weight', models.CharField(default='', max_length=20)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_group_master_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_group_code', models.CharField(max_length=5, unique=True)),
                ('group_name', models.CharField(default='', max_length=100)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_item_map_factory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_item_code', models.CharField(max_length=9)),
                ('factory_name', models.CharField(max_length=5)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_item_master_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_item_code', models.CharField(max_length=9, unique=True)),
                ('description_EN', models.CharField(default='', max_length=50)),
                ('description_TH', models.CharField(default='', max_length=100)),
                ('waste_group_code', models.CharField(default='', max_length=5)),
                ('waste_unit', models.CharField(default='', max_length=5)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Waste_item_price_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waste_item_code', models.CharField(max_length=9, unique=True)),
                ('price', models.FloatField(default=0.0)),
                ('unit_price', models.CharField(default='', max_length=5)),
                ('price_effective_from', models.CharField(default='', max_length=20)),
                ('price_effective_to', models.CharField(default='', max_length=20)),
                ('date_code_from', models.IntegerField(default=0)),
                ('date_code_to', models.IntegerField(default=0)),
                ('company_code', models.CharField(default='', max_length=10)),
                ('systems_date', models.DateField(default=datetime.datetime.now)),
                ('update_date', models.CharField(default='', max_length=20)),
                ('update_by', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
