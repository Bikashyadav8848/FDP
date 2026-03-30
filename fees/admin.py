from django.contrib import admin
from .models import FeeCategory, FeeStructure, StudentFee, FeePayment

@admin.register(FeeCategory)
class FeeCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['name', 'description']
    ordering = ['name']

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'class_section', 'fee_type', 'amount', 'frequency', 'due_date', 'is_active']
    list_filter = ['fee_type', 'frequency', 'is_active', 'category', 'class_section', 'due_date']
    search_fields = ['name', 'category__name', 'class_section__name']
    ordering = ['class_section', 'category', 'name']
    list_editable = ['amount', 'is_active']

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = ['student', 'fee_structure', 'academic_year', 'total_amount', 'paid_amount', 'due_amount', 'status']
    list_filter = ['status', 'academic_year', 'fee_structure__category', 'fee_structure__class_section']
    search_fields = ['student__name', 'student__roll_number', 'fee_structure__name']
    ordering = ['-created_at']
    readonly_fields = ['paid_amount', 'due_amount']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('student', 'fee_structure', 'fee_structure__category', 'fee_structure__class_section')

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ['student_fee', 'amount', 'payment_date', 'payment_method', 'transaction_id']
    list_filter = ['payment_method', 'payment_date']
    search_fields = ['student_fee__student__name', 'student_fee__student__roll_number', 'transaction_id']
    ordering = ['-payment_date']
    date_hierarchy = 'payment_date'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('student_fee', 'student_fee__student')
