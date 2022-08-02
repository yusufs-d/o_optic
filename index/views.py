from turtle import st
from django.shortcuts import get_object_or_404, redirect, render
from .models import Customer,Customer_2, Expense,Expense_2, Income,Income_2
from django.contrib import messages
from datetime import date, datetime
from pytz import timezone
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required(login_url="")
def index(request):
    now_utc = datetime.now(timezone('Europe/Istanbul'))
    now_date = now_utc.strftime('%d.%m.%Y, %H:%M')
    if str(request.user) == "mali":
        customers =Customer_2.objects.all()
    else:
        customers =Customer.objects.all()
    if str(request.user) == "mali":
        incomes = Income_2.objects.all()
    else:
        incomes = Income.objects.all()

    if str(request.user) == "mali":
        last_income = Income_2.objects.all().last()
    else:
        last_income = Income.objects.all().last()

    if str(request.user) == "mali":
        expenses = Expense_2.objects.all()
    else:
        expenses = Expense.objects.all()
    daily_income = 0
    total_income = 0
    total_expense = 0
    customer_count = len(customers)
    if last_income != None:
        if last_income.date == now_date[:10]:
            daily_income = last_income.income_amount

    for income in incomes:
        if(income.date !=""):
           total_income += int(income.income_amount) 

    for expense in expenses:
        total_expense += int(expense.expense_amount)
    variables = {
        "daily_income":daily_income,
        "customer_count":customer_count,
        "total_income" : total_income,
        "total_expense": total_expense,
        "user" : str(request.user)
    }

    return render(request,"index.html",variables)

@staff_member_required(login_url="")
def customer(request):
    if str(request.user) == "mali":
        customers =Customer_2.objects.all()
    else:
        customers =Customer.objects.all()

    return render(request,"customer.html",{"customers":customers})

@staff_member_required(login_url="")
def add_customer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        frame_brand = request.POST.get("frame_brand")
        if frame_brand == "Other":
            frame_brand = request.POST.get("other")
        elif frame_brand == "Markalar":
            frame_brand = ""
        frame_model = request.POST.get("frame_model")
        if frame_model == "Model":
            frame_model = ""
        frame_serial = request.POST.get("frame_serial")
        frame_price = request.POST.get("frame_price")
        if frame_price == "":
            frame_price = 0
        else:
            frame_price = int(frame_price)
        frame_income = request.POST.get("frame_income")
        if frame_income == "":
            frame_income = 0
        else:
            frame_income = int(frame_income)
        if frame_income>frame_price:
            messages.error(request,"Alınan miktar ürün fiyatından yüksek olamaz!")
            return redirect(add_customer)
        frame_payment_method = request.POST.get("frame_payment_method")
        if frame_payment_method =="Ödeme Yöntemi":
            frame_payment_method = ""
        lens_brand = request.POST.get("lens_brand")
        lens_dist_sf_r = request.POST.get("r_sf")
        lens_dist_si_r = request.POST.get("r_si")
        lens_dist_aks_r = request.POST.get("r_aks")
        lens_dist_sf_l = request.POST.get("l_sf")
        lens_dist_si_l = request.POST.get("l_si")
        lens_dist_aks_l = request.POST.get("l_aks")
        lens_cl_sf_r = request.POST.get("ry_sf")
        lens_cl_si_r = request.POST.get("ry_si")
        lens_cl_aks_r = request.POST.get("ry_aks")
        lens_cl_sf_l = request.POST.get("ly_sf")
        lens_cl_si_l = request.POST.get("ly_si")
        lens_cl_aks_l = request.POST.get("ly_aks")
        lens_price = request.POST.get("lens_price")
        if lens_price == "":
            lens_price = 0
        else:
            lens_price = int(lens_price)
        lens_income = request.POST.get("lens_income")
        if lens_income == "":
            lens_income = 0
        else:
            lens_income = int(lens_income)
        if lens_income>lens_price:
            messages.error(request,"Alınan miktar ürün fiyatından yüksek olamaz!")
            return redirect(add_customer)
        lens_payment_method = request.POST.get("lens_payment_method")
        if lens_payment_method =="Ödeme Yöntemi":
            lens_payment_method = ""
        now_utc = datetime.now(timezone('Europe/Istanbul'))
        now_date = now_utc.strftime('%d.%m.%Y, %H:%M')
        if str(request.user) == "mali":
            new_customer = Customer_2(
                name = name,
                phone = phone,
                date = now_date,
                frame_brand = frame_brand,
                frame_model = frame_model,
                frame_serial = frame_serial,
                frame_price = frame_price,
                frame_income = frame_income,
                frame_remain = frame_price-frame_income,
                frame_payment_method = frame_payment_method,
                lens_brand = lens_brand,
                lens_dist_sf_r = lens_dist_sf_r,
                lens_dist_si_r = lens_dist_si_r,
                lens_dist_aks_r = lens_dist_aks_r,
                lens_dist_sf_l = lens_dist_sf_l,
                lens_dist_si_l = lens_dist_si_l,
                lens_dist_aks_l = lens_dist_aks_l,
                lens_cl_sf_r = lens_cl_sf_r,
                lens_cl_si_r = lens_cl_si_r,
                lens_cl_aks_r = lens_cl_aks_r,
                lens_cl_sf_l = lens_cl_sf_l,
                lens_cl_si_l = lens_cl_si_l,
                lens_cl_aks_l = lens_cl_aks_l,
                lens_price = lens_price,
                lens_income = lens_income,
                lens_remain = lens_price-lens_income,
                lens_payment_method = lens_payment_method,
                )
        else:
            new_customer = Customer(
                name = name,
                phone = phone,
                date = now_date,
                frame_brand = frame_brand,
                frame_model = frame_model,
                frame_serial = frame_serial,
                frame_price = frame_price,
                frame_income = frame_income,
                frame_remain = frame_price-frame_income,
                frame_payment_method = frame_payment_method,
                lens_brand = lens_brand,
                lens_dist_sf_r = lens_dist_sf_r,
                lens_dist_si_r = lens_dist_si_r,
                lens_dist_aks_r = lens_dist_aks_r,
                lens_dist_sf_l = lens_dist_sf_l,
                lens_dist_si_l = lens_dist_si_l,
                lens_dist_aks_l = lens_dist_aks_l,
                lens_cl_sf_r = lens_cl_sf_r,
                lens_cl_si_r = lens_cl_si_r,
                lens_cl_aks_r = lens_cl_aks_r,
                lens_cl_sf_l = lens_cl_sf_l,
                lens_cl_si_l = lens_cl_si_l,
                lens_cl_aks_l = lens_cl_aks_l,
                lens_price = lens_price,
                lens_income = lens_income,
                lens_remain = lens_price-lens_income,
                lens_payment_method = lens_payment_method,
                )


        new_customer.save()
        messages.success(request,"Müşteri Başarıyla Kaydedildi")
        return redirect(customer)

    return render(request, "add_customer.html")


@staff_member_required(login_url="")
def delete_customer(request,id):
    if str(request.user) == "mali":
        customer = get_object_or_404(Customer_2,id=id)
    else:
        customer = get_object_or_404(Customer,id=id)

    customer.delete()
    messages.success(request,"Müşteri Başarıyla silindi")
    return redirect("customer")
    
@staff_member_required()
def edit_customer(request,id):
    if str(request.user) == "mali":
        customer = get_object_or_404(Customer_2,id=id)
    else:
        customer = get_object_or_404(Customer,id=id)

    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        no_frame = request.POST.get("is_frame")
        if no_frame == None:
            no_frame = 0
        else:
            no_frame = 1
        frame_brand = request.POST.get("frame_brand")
        if frame_brand == "Other":
            frame_brand = request.POST.get("other")
        elif frame_brand == "Markalar":
            frame_brand = ""
        frame_model = request.POST.get("frame_model")
        if frame_model == "Model":
            frame_model = ""
        frame_serial = request.POST.get("frame_serial")
        frame_price = request.POST.get("frame_price")
        if frame_price == "":
            frame_price = 0
        else:
            frame_price = int(frame_price)
        frame_income = request.POST.get("frame_income")
        if frame_income == "":
            frame_income = 0
        else:
            frame_income = int(frame_income)
        if frame_income>frame_price:
            messages.error(request,"Alınan miktar ürün fiyatından yüksek olamaz!")
            return redirect(add_customer)
        frame_payment_method = request.POST.get("frame_payment_method")
        if frame_payment_method =="Ödeme Yöntemi":
            frame_payment_method = ""
        no_lens = request.POST.get("is_lens")
        if no_lens == None:
            no_lens = 0
        else:
            no_lens = 1
        lens_brand = request.POST.get("lens_brand")
        lens_dist_sf_r = request.POST.get("r_sf")
        lens_dist_si_r = request.POST.get("r_si")
        lens_dist_aks_r = request.POST.get("r_aks")
        lens_dist_sf_l = request.POST.get("l_sf")
        lens_dist_si_l = request.POST.get("l_si")
        lens_dist_aks_l = request.POST.get("l_aks")
        lens_cl_sf_r = request.POST.get("ry_sf")
        lens_cl_si_r = request.POST.get("ry_si")
        lens_cl_aks_r = request.POST.get("ry_aks")
        lens_cl_sf_l = request.POST.get("ly_sf")
        lens_cl_si_l = request.POST.get("ly_si")
        lens_cl_aks_l = request.POST.get("ly_aks")
        lens_price = request.POST.get("lens_price")
        if lens_price == "":
            lens_price = 0
        else:
            lens_price = int(lens_price)
        lens_income = request.POST.get("lens_income")
        if lens_income == "":
            lens_income = 0
        else:
            lens_income = int(lens_income)
        if lens_income>lens_price:
            messages.error(request,"Alınan miktar ürün fiyatından yüksek olamaz!")
            return redirect(add_customer)
        lens_payment_method = request.POST.get("lens_payment_method")
        if lens_payment_method =="Ödeme Yöntemi":
            lens_payment_method = ""
        
        customer.name = name
        customer.phone = phone
        customer.frame_brand = frame_brand
        customer.frame_model = frame_model
        customer.frame_serial = frame_serial
        customer.frame_price = frame_price
        customer.frame_income = frame_income
        customer.frame_remain = frame_price-frame_income
        customer.frame_payment_method = frame_payment_method
        customer.lens_brand = lens_brand
        customer.lens_dist_sf_r = lens_dist_sf_r
        customer.lens_dist_si_r = lens_dist_si_r
        customer.lens_dist_aks_r = lens_dist_aks_r
        customer.lens_dist_sf_l = lens_dist_sf_l
        customer.lens_dist_si_l = lens_dist_si_l
        customer.lens_dist_aks_l = lens_dist_aks_l
        customer.lens_cl_sf_r = lens_cl_sf_r
        customer.lens_cl_si_r = lens_cl_si_r
        customer.lens_cl_aks_r = lens_cl_aks_r
        customer.lens_cl_sf_l = lens_cl_sf_l
        customer.lens_cl_si_l = lens_cl_si_l
        customer.lens_cl_aks_l = lens_cl_aks_l
        customer.lens_price = lens_price
        customer.lens_income = lens_income
        customer.lens_remain = lens_price-lens_income
        customer.lens_payment_method = lens_payment_method
        customer.save()
        messages.success(request,"Müşteri Başarıyla Güncellendi")
        return redirect("customer")
    return render(request,"edit_customer.html",{"customer":customer})

@staff_member_required(login_url="")
def debts(request):
    if str(request.user) == "mali":
        customers =Customer_2.objects.all()
    else:
        customers =Customer.objects.all()
    return render(request,"debts.html",{"customers":customers})

@staff_member_required()
def income(request):
    if str(request.user) == "mali":
        customers =Customer_2.objects.all()
    else:
        customers =Customer.objects.all()
    if str(request.user) == "mali":
        expenses =Expense_2.objects.all()
    else:
        expenses =Expense.objects.all()
    now_utc = datetime.now(timezone('Europe/Istanbul'))
    now_date = now_utc.strftime('%d.%m.%Y, %H:%M')
    now_date_edited = now_date[:11]+"..."
    daily_income = 0
    daily_expense = 0
    dates = list()
    for customer in customers:
        dates.append(customer.date[:10])
        if customer.date[:11]+"..." == now_date_edited:
            daily_income += int(customer.frame_income)+int(customer.lens_income)

    dates = list(set(dates))
    
    for d in dates:
        if str(request.user) == "mali":
            inc_dates = Income_2.objects.get_or_create(date = d)
        else:
            inc_dates = Income.objects.get_or_create(date = d)



    for expense in expenses:
        
        if expense.date[:11]+"..." == now_date_edited:
            daily_expense += -1*int(expense.expense_amount)
    if len(dates)>0:
        if(now_date[:10] == dates[-1] ):
            if str(request.user) == "mali":
                inc = get_object_or_404(Income_2,date=dates[-1])
            else:
                inc = get_object_or_404(Income,date=dates[-1])
            inc.income_amount = daily_income-(-1*daily_expense)
            inc.save()
    else:
        if str(request.user) == "mali":
            inc = get_object_or_404(Income_2,date=now_date[:10])
        else:
            inc = get_object_or_404(Income,date=now_date[:10])

        inc.income_amount = daily_expense
        inc.save()



        


    if str(request.user) == "mali":
        all_incomes = Income_2.objects.all()
    else:
        all_incomes = Income.objects.all()



        


    variables = {"customers":customers,
                "now":now_date,
                "daily_income":daily_income,
                "expenses":expenses,
                "daily_expense":daily_expense,
                "incomes": all_incomes
          }
    return render(request,"income.html",variables)

@staff_member_required(login_url="")
def add_expense(request):
    now_utc = datetime.now(timezone('Europe/Istanbul'))
    now_date = now_utc.strftime('%d.%m.%Y, %H:%M')
    if request.method == "POST":
        name = request.POST.get("expense_name")
        expense_amount = request.POST.get("expense_amount")
        expense_payment_method = request.POST.get("expense_payment_method")
        if str(request.user) == "mali":
            new_expense = Expense_2(
                name = name, 
                date = now_date,
                expense_amount = expense_amount, 
                expense_payment_method = expense_payment_method
            )
        else:
            new_expense = Expense(
                name = name, 
                date = now_date,
                expense_amount = expense_amount, 
                expense_payment_method = expense_payment_method
            )            
        new_expense.save()
        messages.success(request,"Gider Başarıyla Kaydedildi")
        return redirect("income")

@staff_member_required()
def delete_expense(request,id):
    if str(request.user) == "mali":
        expense = get_object_or_404(Expense_2,id=id)
    else:
        expense = get_object_or_404(Expense,id=id)
    expense.delete()
    messages.success(request,"Gider Başarıyla silindi")
    return redirect("income")
