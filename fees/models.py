from django.db import models
from students.models import Student
from classes.models import Class

class FeeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text="e.g., Tuition, Transportation, Library")
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fee Category'
        verbose_name_plural = 'Fee Categories'
        ordering = ['name']

    def __str__(self):
        return self.name

class FeeStructure(models.Model):
    FEE_TYPE_CHOICES = [
        ('fixed', 'Fixed Amount'),
        ('percentage', 'Percentage of Base Fee'),
    ]

    FREQUENCY_CHOICES = [
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('half_yearly', 'Half Yearly'),
        ('yearly', 'Yearly'),
        ('one_time', 'One Time'),
    ]

    name = models.CharField(max_length=200, help_text="e.g., Class 10 Tuition Fee")
    category = models.ForeignKey(FeeCategory, on_delete=models.CASCADE)
    class_section = models.ForeignKey(Class, on_delete=models.CASCADE)
    fee_type = models.CharField(max_length=20, choices=FEE_TYPE_CHOICES, default='fixed')
    amount = models.DecimalField(max_digits=10, decimal_places=2, help_text="Amount in rupees")
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES, default='monthly')
    due_date = models.DateField(help_text="Due date for payment")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fee Structure'
        verbose_name_plural = 'Fee Structures'
        ordering = ['class_section', 'category', 'name']

    def __str__(self):
        return f"{self.class_section} - {self.name} - ₹{self.amount}"

class StudentFee(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('partially_paid', 'Partially Paid'),
        ('paid', 'Paid'),
        ('overdue', 'Overdue'),
        ('waived', 'Waived'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    fee_structure = models.ForeignKey(FeeStructure, on_delete=models.CASCADE)
    academic_year = models.CharField(max_length=20, help_text="e.g., 2024-2025")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    due_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Student Fee'
        verbose_name_plural = 'Student Fees'
        ordering = ['-created_at']
        unique_together = ['student', 'fee_structure', 'academic_year']

    def __str__(self):
        return f"{self.student} - {self.fee_structure} - {self.status}"

    def save(self, *args, **kwargs):
        self.due_amount = self.total_amount - self.paid_amount
        if self.due_amount <= 0:
            self.status = 'paid'
        elif self.paid_amount > 0:
            self.status = 'partially_paid'
        super().save(*args, **kwargs)

class FeePayment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('cash', 'Cash'),
        ('online', 'Online Transfer'),
        ('cheque', 'Cheque'),
        ('card', 'Card'),
    ]

    student_fee = models.ForeignKey(StudentFee, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='cash')
    transaction_id = models.CharField(max_length=100, blank=True, null=True, help_text="Online transaction ID or receipt number")
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Fee Payment'
        verbose_name_plural = 'Fee Payments'
        ordering = ['-payment_date']

    def __str__(self):
        return f"{self.student_fee.student} - ₹{self.amount} - {self.payment_date}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Update the student fee totals
        student_fee = self.student_fee
        total_paid = student_fee.payments.aggregate(total=models.Sum('amount'))['total'] or 0
        student_fee.paid_amount = total_paid
        student_fee.save()
