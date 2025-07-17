# Hospital Management Database (HospitalManagementDB)

This project simulates a Hospital Management System built entirely in SQL using PostgreSQL. It was designed to demonstrate core database administration (DBA) skills including schema design, data seeding, backups, role-based access control, triggers, functions, and reporting.

## 🏥 Project Overview

- **Database Name:** `hospital_db`
- **Platform:** PostgreSQL (with pgAdmin or psql)
- **Focus:** Hands-on experience with practical SQL features used in real-world healthcare systems.

## 🧱 Schema Design

The database includes the following entities:

- `Patients`
- `Doctors`
- `Departments`
- `Appointments`
- `Medications`
- `Prescriptions`

Each table is designed with appropriate primary and foreign keys, normalization, and real-world constraints.

## 📦 Files Included

| File Name             | Description                                         |
|----------------------|-----------------------------------------------------|
| `schema.sql`          | SQL script to create all database tables           |
| `seed_data.sql`       | Script to populate the database with sample data   |
| `role_and_permissions.sql` | SQL for creating roles and granting permissions |
| `reporting_queries.sql`    | Analytical queries for reports                 |
| `functions.sql`       | Custom PL/pgSQL functions                          |
| `triggers.sql`        | Audit logging with triggers                        |
| `backup/hospital_db_backup.sql` | pg_dump file of the database             |

## 🧪 Key Features Demonstrated

- ✅ Relational database schema design
- ✅ PL/pgSQL stored procedures
- ✅ User roles and permission management
- ✅ Triggers for audit logging
- ✅ Backup and restore with `pg_dump` and `pg_restore`
- ✅ Practical SQL reporting for analytics

## 🔎 Sample Reporting Queries

- Appointments with patient and doctor names
- Patient prescription history
- Appointment status counts
- Number of patients seen per doctor

## 📸 Screenshots

_Screenshots of your pgAdmin tables, queries, or ER diagram can go here (optional)._

## 🚀 Getting Started

1. Clone the repo:
   ```bash
   git clone https://github.com/DBA-GibsonN/HospitalManagementDB.git
   cd HospitalManagementDB
   ```

2. Create the database:
   ```sql
   CREATE DATABASE hospital_db;
   ```

3. Execute the scripts in order:
   - `schema.sql`
   - `seed_data.sql`
   - `role_and_permissions.sql`
   - `functions.sql`
   - `triggers.sql`

4. Run and explore queries in `reporting_queries.sql`.

5. (Optional) Restore from backup:
   ```bash
   pg_restore -U your_user -d hospital_db backup/hospital_db_backup.sql
   ```

## 👤 Author

**Gibson**  
Aspiring Database Administrator  
GitHub: [DBA-GibsonN](https://github.com/DBA-GibsonN)

## 🏁 Next Steps

- Add advanced procedures and views
- Implement API or frontend for full-stack showcase
- Deploy using Docker or on a cloud database

---

> _This project was built as part of my journey to become a professional Database Administrator. Feedback is welcome!_
