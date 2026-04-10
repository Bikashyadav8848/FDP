# 🎓 Modern Student Management System (SMS)

A sleek, sidebar-first Django application for modern school administration. This project features a responsive dashboard, automated fee management, and dynamic system settings.

## ✨ Key Features
- **Modern UI**: Professional sidebar-based navigation with a responsive layout.
- **Dynamic Themes**: Change application colors (Indigo, Sapphire, Emerald, Slate) in real-time via settings.
- **Fees Management**: Interactive dashboard to track expected revenue, collections, and dues.
- **Global Settings**: Manage institution name, academic year, and system-wide notifications.
- **Module Tracking**: Complete records for Students, Teachers, Attendance, Marks, and Timetables.

---

## 🚀 Quick Setup (New Laptop)

Follow these simple steps to run this project on a new system.

### Step 1: Clone the Project
```bash
git clone https://github.com/Bikashyadav8848/SMS.git
cd SMS
```

### Step 2: Create Virtual Environment
```powershell
python -m venv venv
```

### Step 3: Allow PowerShell Scripts (if needed)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 4: Activate Virtual Environment
```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Required Packages
```bash
pip install -r requirements.txt
```

### Step 6: Setup Database
```bash
python manage.py migrate
```

### Step 7: Create Admin User (optional)
```bash
python manage.py createsuperuser
```

### Step 8: Run the Project
```bash
python manage.py runserver
```

### Step 9: Open in Browser
Go to: http://127.0.0.1:8000/



---

## 🌍 Accessing the App
Once the server is running, open your browser and go to:
- **Dashboard**: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Admin Panel**: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 👨‍💻 Powered By
✨ **Bikash Kumar Yadav** ✨
*Modernizing school administration with Django & Python*

---

## 👥 Contributors
- **MD Majid Khan**
- **Bikesh Yadav**
- **Raj Gimbhal**
- **Kishor Shah**
- **Aksh Koli**
- **Rahul Jadhav**

