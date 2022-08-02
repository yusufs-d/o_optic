from django.db import models
from sqlalchemy import true

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=50)
    phone = models.CharField(verbose_name="phone",max_length=50)
    date = models.CharField(max_length=20, verbose_name="date")
    frame_brand = models.CharField(verbose_name="frame_brand", max_length=30)
    frame_model = models.CharField(verbose_name="frame_model", max_length=10)
    frame_serial = models.CharField(verbose_name="frame_serial",max_length=50)
    frame_price = models.CharField(verbose_name="frame_price",max_length=10)
    frame_income = models.CharField(verbose_name="frame_income",max_length=10)
    frame_remain = models.CharField(verbose_name="frame_remain",max_length=10)
    frame_payment_method = models.CharField(verbose_name="frame_payment_method", max_length=10)
    lens_brand = models.CharField(verbose_name="lens_brand", max_length=30)
    lens_dist_sf_r = models.CharField(verbose_name="lens_dist_sf_r", max_length=10)
    lens_dist_si_r = models.CharField(verbose_name="lens_dist_si_r", max_length=10)
    lens_dist_aks_r = models.CharField(verbose_name="lens_dist_aks_r", max_length=10)
    lens_dist_sf_l = models.CharField(verbose_name="lens_dist_sf_l", max_length=10)
    lens_dist_si_l = models.CharField(verbose_name="lens_dist_si_l", max_length=10)
    lens_dist_aks_l = models.CharField(verbose_name="lens_dist_aks_l", max_length=10)
    lens_cl_sf_r = models.CharField(verbose_name="lens_cl_sf_r", max_length=10)
    lens_cl_si_r = models.CharField(verbose_name="lens_cl_si_r", max_length=10)
    lens_cl_aks_r = models.CharField(verbose_name="lens_cl_aks_r", max_length=10)
    lens_cl_sf_l = models.CharField(verbose_name="lens_cl_sf_l", max_length=10)
    lens_cl_si_l = models.CharField(verbose_name="lens_cl_si_l", max_length=10)
    lens_cl_aks_l = models.CharField(verbose_name="lens_cl_aks_l", max_length=10)
    lens_price = models.CharField(verbose_name="lens_price", max_length=10)
    lens_income = models.CharField(verbose_name="lens_income", max_length=10)
    lens_remain = models.CharField(verbose_name="lens_remain",max_length=10)
    lens_payment_method = models.CharField(verbose_name="lens_payment_method", max_length=10)


class Customer_2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=50)
    phone = models.CharField(verbose_name="phone",max_length=50)
    date = models.CharField(max_length=20, verbose_name="date")
    frame_brand = models.CharField(verbose_name="frame_brand", max_length=30)
    frame_model = models.CharField(verbose_name="frame_model", max_length=10)
    frame_serial = models.CharField(verbose_name="frame_serial",max_length=50)
    frame_price = models.CharField(verbose_name="frame_price",max_length=10)
    frame_income = models.CharField(verbose_name="frame_income",max_length=10)
    frame_remain = models.CharField(verbose_name="frame_remain",max_length=10)
    frame_payment_method = models.CharField(verbose_name="frame_payment_method", max_length=10)
    lens_brand = models.CharField(verbose_name="lens_brand", max_length=30)
    lens_dist_sf_r = models.CharField(verbose_name="lens_dist_sf_r", max_length=10)
    lens_dist_si_r = models.CharField(verbose_name="lens_dist_si_r", max_length=10)
    lens_dist_aks_r = models.CharField(verbose_name="lens_dist_aks_r", max_length=10)
    lens_dist_sf_l = models.CharField(verbose_name="lens_dist_sf_l", max_length=10)
    lens_dist_si_l = models.CharField(verbose_name="lens_dist_si_l", max_length=10)
    lens_dist_aks_l = models.CharField(verbose_name="lens_dist_aks_l", max_length=10)
    lens_cl_sf_r = models.CharField(verbose_name="lens_cl_sf_r", max_length=10)
    lens_cl_si_r = models.CharField(verbose_name="lens_cl_si_r", max_length=10)
    lens_cl_aks_r = models.CharField(verbose_name="lens_cl_aks_r", max_length=10)
    lens_cl_sf_l = models.CharField(verbose_name="lens_cl_sf_l", max_length=10)
    lens_cl_si_l = models.CharField(verbose_name="lens_cl_si_l", max_length=10)
    lens_cl_aks_l = models.CharField(verbose_name="lens_cl_aks_l", max_length=10)
    lens_price = models.CharField(verbose_name="lens_price", max_length=10)
    lens_income = models.CharField(verbose_name="lens_income", max_length=10)
    lens_remain = models.CharField(verbose_name="lens_remain",max_length=10)
    lens_payment_method = models.CharField(verbose_name="lens_payment_method", max_length=10)


class Income(models.Model):
    id = models.AutoField(primary_key=True)
    income_amount = models.CharField(verbose_name="income_amount",max_length=10)
    date = models.CharField(max_length=20, verbose_name="date")

class Income_2(models.Model):
    id = models.AutoField(primary_key=True)
    income_amount = models.CharField(verbose_name="income_amount",max_length=10)
    date = models.CharField(max_length=20, verbose_name="date")


class Expense(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=50)
    date = models.CharField(max_length=20, verbose_name="date")
    expense_amount = models.CharField(verbose_name="expense_amount",max_length=10)
    expense_payment_method = models.CharField(verbose_name="expense_payment_method", max_length=10)

class Expense_2(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="name",max_length=50)
    date = models.CharField(max_length=20, verbose_name="date")
    expense_amount = models.CharField(verbose_name="expense_amount",max_length=10)
    expense_payment_method = models.CharField(verbose_name="expense_payment_method", max_length=10)


    




