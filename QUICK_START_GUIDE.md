# 🚀 Quick Start Guide - Django Student Management System

## ⚡ 5-Minute Setup

### Step 1: Navigate to Project
```bash
cd full_django_sms
```

### Step 2: Start Django Server
```bash
python manage.py runserver
```

### Step 3: Open Application
```
http://localhost:8000
```

---

## 📊 Dashboard Overview

When you first load the application, you'll see the **Home Dashboard** with:

### Feature Cards (8 Modules)
- 👥 **Students** - Manage student records
- 👨‍🏫 **Teachers** - Manage teacher information
- 📚 **Classes** - Manage class sections
- 📖 **Subjects** - Manage subjects and teacher assignments
- ✅ **Attendance** - Track daily attendance
- 📅 **Timetable** - Create weekly schedules
- 💰 **Fees** - Manage student fees and payments
- 📝 **Marks** - Record student grades

### Statistics
- Total count for each module
- Fee statistics (Assigned, Paid, Due amounts)
- Quick navigation to each module

---

## 🎯 Using Each Module

### 1️⃣ STUDENTS Module

**View All Students**
- Click "Students" in navigation
- See all student records in card format
- Each card shows: Name, Email, Roll Number

**Add New Student**
1. Click "Students" → "Add Student Record"
2. Fill in:
   - **Name**: Full name of student
   - **Email**: Student's email
   - **Roll Number**: Unique identifier
3. Click "Add Student"

**Edit Student**
1. Go to Students list
2. Click edit icon (✏️) on any student card
3. Modify details
4. Click "Update Student"

**Delete Student**
1. Go to Students list
2. Click delete icon (🗑️) on student card
3. Confirm deletion

---

### 2️⃣ TEACHERS Module

**View All Teachers**
- Click "Teachers" in navigation
- See all teacher records with their assigned subjects

**Add New Teacher**
1. Click "Teachers" → "Add Teacher"
2. Fill in:
   - **Name**: Teacher's full name
   - **Subject**: Subject they teach
3. Click "Add Teacher"

**Edit Teacher**
1. Go to Teachers list
2. Click edit icon on teacher card
3. Modify name or subject
4. Click "Update Teacher"

---

### 3️⃣ CLASSES Module

**View All Classes**
- Click "Classes" in navigation
- See all class sections

**Add New Class**
1. Click "Classes" → "Add Class"
2. Fill in:
   - **Name**: Class name (e.g., "Class X", "Grade 10")
   - **Section**: Section letter (e.g., "A", "B", "C")
3. Click "Add Class"

---

### 4️⃣ SUBJECTS Module

**View All Subjects**
- Click "Subjects" in navigation
- See subjects with assigned teachers

**Add New Subject**
1. Click "Subjects" → "Add Subject"
2. Fill in:
   - **Name**: Subject name (e.g., "Mathematics")
   - **Code**: Subject code (e.g., "MATH101")
   - **Teacher**: Select from dropdown
3. Click "Add Subject"

---

### 5️⃣ ATTENDANCE Module ⭐ *Recently Enhanced*

**View Attendance Records**
1. Click "Attendance" in navigation
2. See all attendance records with filters

**Filter Attendance**
1. **By Student**: Type student name in search box
2. **By Date Range**: Select "From Date" and "To Date"
3. Click "Apply Filters"

**View Statistics**
- **Present Count**: Number of present records shown
- **Absent Count**: Number of absent records shown
- **Leave Count**: Number of leave records shown
- **Total Records**: Total attendance entries

**Mark Attendance**
1. Click "Add Attendance Record"
2. Select:
   - **Student**: Pick from dropdown
   - **Date**: Select date
   - **Status**: Click on Present/Absent/Leave button
3. Click "Add Attendance"

**Edit/Delete Attendance**
- Use edit (✏️) and delete (🗑️) icons on each record

---

### 6️⃣ TIMETABLE Module

**View Weekly Timetable**
1. Click "Timetable" in navigation
2. See the entire week's schedule
3. **Left column**: Time periods (Period 1-7)
4. **Top row**: Days (Monday-Sunday)
5. **Grid cells**: Subject and teacher name

**Create Timetable Entry**
1. Click "Timetable" → "Add Timetable Entry"
2. Fill in:
   - **Class**: Select class
   - **Subject**: Select subject
   - **Teacher**: Auto-filled based on subject
   - **Time Slot**: Select period (1-7)
   - **Day of Week**: Select day
3. Click "Add Timetable"

---

### 7️⃣ FEES Module ⭐ *Complete Management System*

**Fees Dashboard**
- Click "Fees" in navigation
- Shows:
  - Total fee categories
  - Total fee structures
  - Student fee assignments
  - Fee payments recorded
  - Quick action buttons

#### Fee Categories
**View Categories**
1. Click "Fees" → "Fee Categories"
2. See predefined categories:
   - 💰 Tuition
   - 🚌 Transportation
   - 📚 Library
   - 📝 Exam

**Add New Category**
1. Click "Add Fee Category"
2. Fill in:
   - **Name**: Category name
   - **Description**: What the fee covers
3. Click "Add Category"

#### Fee Structures
**View Structures**
1. Click "Fees" → "Fee Structures"
2. See fee amount structure for classes
3. Filter by Class or Category

**Create Fee Structure**
1. Click "Add Fee Structure"
2. Fill in:
   - **Amount**: Fee amount (e.g., 5000)
   - **Category**: Select category (Tuition, etc.)
   - **Class**: Which class this applies to
   - **Frequency**: Monthly/Quarterly/Annually
   - **Due Date**: When payment is due
3. Click "Add Structure"

#### Student Fees
**View Student Fees**
1. Click "Fees" → "Student Fees"
2. See all students' fee assignments
3. Shows:
   - Student name
   - Total amount
   - Paid amount
   - Due amount (auto-calculated)
   - Payment status (Pending/Partial/Paid)

**Assign Fee to Student**
1. Click "Add Student Fee"
2. Fill in:
   - **Student**: Select student
   - **Fee Structure**: Select structure
   - **Total Amount**: Amount to be paid
3. Click "Add Student Fee"

#### Fee Payments
**View Payments**
1. Click "Fees" → "Fee Payments"
2. See all payment records
3. Filter by date range if needed

**Record Payment**
1. Click "Record Payment"
2. Fill in:
   - **Student Fee**: Select student's fee
   - **Amount**: Amount paid
   - **Payment Method**: Cash/Check/Online/Bank Transfer
   - **Transaction ID**: Reference number
   - **Payment Date**: When paid
3. Click "Record Payment"

---

### 8️⃣ MARKS Module

**View Marks**
1. Click "Marks" in navigation
2. See all recorded grades

**Add Marks**
1. Click "Add Mark"
2. Fill in:
   - **Student**: Select student
   - **Subject**: Select subject
   - **Marks**: Score (e.g., 95)
3. Click "Add Mark"

---

## 🔍 Advanced Features

### Filtering & Search

**Attendance Filter Example**
```
Search for: "Rahul"
From Date: 2026-03-01
To Date: 2026-03-18
Click "Apply Filters" → Shows only Rahul's attendance for that period
```

**Fees Filter Example**
```
Select Class: "Class X-A"
Select Category: "Tuition"
Click "Filter" → Shows only tuition fees for that class
```

### Statistics

**Attendance Statistics**
- Auto-calculated based on filters
- Shows counts of Present, Absent, Leave, Total
- Updates when you change filters

**Fee Statistics**
- Total assigned: Sum of all student fee amounts
- Total paid: Sum of all payments
- Total due: Automatically calculated (assigned - paid)

---

## 🎨 Understanding the Design

### Color Coding
Each module has its own color for easy identification:

| Module | Color | Icon |
|--------|-------|------|
| Students | Indigo | 👥 |
| Teachers | Green | 👨‍🏫 |
| Classes | Cyan | 📚 |
| Subjects | Amber | 📖 |
| Attendance | Purple | ✅ |
| Timetable | Rose | 📅 |
| Fees | Blue | 💰 |
| Marks | Emerald | 📝 |

### Status Badges
- 🟢 **Present** - Green badge
- 🔴 **Absent** - Red badge
- 🟡 **Leave** - Yellow badge
- 🟢 **Paid** - Green badge
- 🟡 **Partial** - Yellow badge
- 🔴 **Pending** - Red badge

### Card Layout
- Each record displays as a card
- Shows relevant information at a glance
- Action buttons (Edit/Delete) at the top right
- Easy to scan and navigate

---

## ⚙️ Common Tasks

### Task: Set up a class timetable

**Step 1**: Create class (if not exists)
- Go to Classes → Add Class
- Name: "Class X", Section: "A"

**Step 2**: Create subject (if not exists)
- Go to Subjects → Add Subject
- Assign a teacher

**Step 3**: Create timetable entries
- Go to Timetable → Add Entry
- For each period and day, select:
  - Class: "Class X-A"
  - Subject: Your subject
  - Time Slot: Period 1-7
  - Day: Monday-Sunday

**Result**: Complete weekly timetable visible on Timetable page

---

### Task: Track and manage fees

**Step 1**: Create fee structure (usually done once)
- Go to Fees → Fee Structures → Add
- Set amount, category, class, frequency

**Step 2**: Assign fees to students
- Go to Fees → Student Fees → Add
- Select student and fee structure

**Step 3**: Record payments
- Go to Fees → Fee Payments → Add Payment
- Record each payment received

**Step 4**: Monitor status
- Go to Fees dashboard
- See total assigned, paid, and due amounts
- Identify pending fees

---

### Task: Track student attendance

**Step 1**: Mark attendance daily
- Go to Attendance → Add Record
- Select student, date, and status

**Step 2**: View attendance report
- Go to Attendance
- Filter by date range or student name
- View statistics

**Step 3**: Export (if needed)
- Contact admin for export functionality

---

## ❓ FAQs

**Q: How do I create admin account?**
A: It's already created during setup. Use credentials from setup step.

**Q: Can I edit a record?**
A: Yes! Click the edit icon (✏️) on any record to modify it.

**Q: Can I delete a record?**
A: Yes! Click the delete icon (🗑️) to remove it (confirmation required).

**Q: Where do I see statistics?**
A: On Home page for system-wide, or in each module for specific stats.

**Q: How do I filter records?**
A: Use the filter form at the top of each list page.

**Q: What is the payment status automatically calculated based on?**
A: Total Amount vs Paid Amount:
- Paid = Total → Status: Paid
- Paid = 0 → Status: Pending  
- 0 < Paid < Total → Status: Partial

**Q: Can I have different timetables for different classes?**
A: Yes! Each timetable entry specifies a class.

**Q: How do I track attendance statistics?**
A: Attend Attendance page - statistics auto-calculate based on filtered records.

---

## 🆘 Troubleshooting

**Server won't start:**
```bash
# Clear cache and restart
python manage.py collectstatic --noinput
python manage.py runserver
```

**Database errors:**
```bash
# Reapply migrations
python manage.py migrate
```

**"Object not found" errors:**
- Ensure you've created records (students, teachers, classes)
- Try refreshing the page

**Dropdown is empty:**
- Create records in the referenced table first
- Example: Create Subject before assigning to Timetable

---

## 📱 Mobile Access

The system is fully responsive! Access from:
- **Desktop**: http://localhost:8000
- **Mobile**: Same URL on your network
- **Tablet**: Works perfectly with touch inputs

---

## 🔐 Admin Panel

Access the advanced admin panel:
```
http://localhost:8000/admin/
```

Login with credentials created during setup.

**Admin Features:**
- Direct database management
- Advanced filtering
- Bulk operations
- Search across all fields
- Record counts and statistics

---

## 📞 Support

For more information, refer to:
- `PROJECT_COMPLETION_SUMMARY.md` - Full technical documentation
- Django docs: https://docs.djangoproject.com/
- Bootstrap docs: https://getbootstrap.com/

---

**Happy Managing!** 🎓

---

*Last Updated: March 18, 2026*
*Django Student Management System v1.0*
