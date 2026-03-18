from django.urls import path
from . import views

urlpatterns = [
    # Dashboard
    path('', views.fees_dashboard, name='fees_dashboard'),

    # Fee Categories
    path('categories/', views.FeeCategoryListView.as_view(), name='fee_categories'),
    path('categories/create/', views.FeeCategoryCreateView.as_view(), name='fee_category_create'),
    path('categories/<int:pk>/update/', views.FeeCategoryUpdateView.as_view(), name='fee_category_update'),
    path('categories/<int:pk>/delete/', views.FeeCategoryDeleteView.as_view(), name='fee_category_delete'),

    # Fee Structures
    path('structures/', views.FeeStructureListView.as_view(), name='fee_structures'),
    path('structures/create/', views.FeeStructureCreateView.as_view(), name='fee_structure_create'),
    path('structures/<int:pk>/update/', views.FeeStructureUpdateView.as_view(), name='fee_structure_update'),
    path('structures/<int:pk>/delete/', views.FeeStructureDeleteView.as_view(), name='fee_structure_delete'),

    # Student Fees
    path('student-fees/', views.StudentFeeListView.as_view(), name='student_fees'),
    path('student-fees/create/', views.StudentFeeCreateView.as_view(), name='student_fee_create'),
    path('student-fees/<int:pk>/update/', views.StudentFeeUpdateView.as_view(), name='student_fee_update'),
    path('student-fees/<int:pk>/delete/', views.StudentFeeDeleteView.as_view(), name='student_fee_delete'),

    # Fee Payments
    path('payments/', views.FeePaymentListView.as_view(), name='fee_payments'),
    path('payments/create/', views.FeePaymentCreateView.as_view(), name='fee_payment_create'),
    path('payments/<int:pk>/update/', views.FeePaymentUpdateView.as_view(), name='fee_payment_update'),
    path('payments/<int:pk>/delete/', views.FeePaymentDeleteView.as_view(), name='fee_payment_delete'),
]