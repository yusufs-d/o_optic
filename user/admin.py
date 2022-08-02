from django.contrib import admin
from index.models import Customer,Expense,Income

# Register your models here.

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["name","date","phone"]
    list_filter = ["date"]
    search_fields = ["title"]
    
    class Meta:
        model = Customer

@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ["date","income_amount"]
    list_filter = ["date"]
    search_fields = ["title"]
    
    class Meta:
        model = Income

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ["name","date","expense_amount"]
    list_filter = ["date"]
    search_fields = ["title"]
    
    class Meta:
        model = Expense

admin.site.site_header = "Kontrol Paneli"
