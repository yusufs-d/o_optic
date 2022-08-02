# Generated by Django 3.2.7 on 2022-08-01 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_alter_customer_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('phone', models.CharField(max_length=50, verbose_name='phone')),
                ('date', models.CharField(max_length=20, verbose_name='date')),
                ('frame_brand', models.CharField(max_length=30, verbose_name='frame_brand')),
                ('frame_model', models.CharField(max_length=10, verbose_name='frame_model')),
                ('frame_serial', models.CharField(max_length=50, verbose_name='frame_serial')),
                ('frame_price', models.CharField(max_length=10, verbose_name='frame_price')),
                ('frame_income', models.CharField(max_length=10, verbose_name='frame_income')),
                ('frame_remain', models.CharField(max_length=10, verbose_name='frame_remain')),
                ('frame_payment_method', models.CharField(max_length=10, verbose_name='frame_payment_method')),
                ('lens_brand', models.CharField(max_length=30, verbose_name='lens_brand')),
                ('lens_dist_sf_r', models.CharField(max_length=10, verbose_name='lens_dist_sf_r')),
                ('lens_dist_si_r', models.CharField(max_length=10, verbose_name='lens_dist_si_r')),
                ('lens_dist_aks_r', models.CharField(max_length=10, verbose_name='lens_dist_aks_r')),
                ('lens_dist_sf_l', models.CharField(max_length=10, verbose_name='lens_dist_sf_l')),
                ('lens_dist_si_l', models.CharField(max_length=10, verbose_name='lens_dist_si_l')),
                ('lens_dist_aks_l', models.CharField(max_length=10, verbose_name='lens_dist_aks_l')),
                ('lens_cl_sf_r', models.CharField(max_length=10, verbose_name='lens_cl_sf_r')),
                ('lens_cl_si_r', models.CharField(max_length=10, verbose_name='lens_cl_si_r')),
                ('lens_cl_aks_r', models.CharField(max_length=10, verbose_name='lens_cl_aks_r')),
                ('lens_cl_sf_l', models.CharField(max_length=10, verbose_name='lens_cl_sf_l')),
                ('lens_cl_si_l', models.CharField(max_length=10, verbose_name='lens_cl_si_l')),
                ('lens_cl_aks_l', models.CharField(max_length=10, verbose_name='lens_cl_aks_l')),
                ('lens_price', models.CharField(max_length=10, verbose_name='lens_price')),
                ('lens_income', models.CharField(max_length=10, verbose_name='lens_income')),
                ('lens_remain', models.CharField(max_length=10, verbose_name='lens_remain')),
                ('lens_payment_method', models.CharField(max_length=10, verbose_name='lens_payment_method')),
            ],
        ),
        migrations.CreateModel(
            name='Expense_2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('date', models.CharField(max_length=20, verbose_name='date')),
                ('expense_amount', models.CharField(max_length=10, verbose_name='expense_amount')),
                ('expense_payment_method', models.CharField(max_length=10, verbose_name='expense_payment_method')),
            ],
        ),
        migrations.CreateModel(
            name='Income_2',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('income_amount', models.CharField(max_length=10, verbose_name='income_amount')),
                ('date', models.CharField(max_length=20, verbose_name='date')),
            ],
        ),
    ]