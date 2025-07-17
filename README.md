
# 🏥 Hospital Management Database (PostgreSQL)

A realistic PostgreSQL-based hospital database designed and developed by **Gibson (DBA-GibsonN)** to showcase hands-on database administration and development skills. This project simulates the key operations of a hospital including patient records, appointments, prescriptions, and reporting with auditing and stored procedures.

---

## 📦 Features

- ✅ Normalized schema with 6+ interconnected tables
- ✅ Sample data for patients, doctors, appointments, medications
- ✅ Stored functions for retrieving patient history
- ✅ Reporting queries for business intelligence
- ✅ Audit logging using triggers on patient updates
- ✅ Role and permission setup
- ✅ Backup and restore with `pg_dump`
- ✅ Version-controlled with Git & SQL scripts

---

## 🛠 Tech Stack

- **Database:** PostgreSQL 15+
- **Editor:** VS Code
- **Tools:** Git, Bash, pgAdmin (optional)
- **Language:** SQL, PL/pgSQL

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/DBA-GibsonN/hospital-db.git
cd hospital-db
```

### 2. Create and Connect to the Database

```bash
createdb hospital_db
psql -d hospital_db
```

### 3. Run the SQL Scripts in Order

```sql
-- 1. Schema
\i schema.sql

-- 2. Seed Data
\i seed_data.sql

-- 3. Roles & Permissions
\i role_and_permissions.sql

-- 4. Functions
\i functions.sql

-- 5. Reporting Queries
\i reporting_queries.sql

-- 6. Triggers
\i audit_trigger.sql
```

---

## 📂 File Structure

| File | Description |
|------|-------------|
| `schema.sql` | Creates all database tables |
| `seed_data.sql` | Inserts sample data |
| `role_and_permissions.sql` | Adds users and roles |
| `functions.sql` | Functions like `GetPatientAppointments()` |
| `reporting_queries.sql` | Useful queries for insights |
| `audit_trigger.sql` | Adds audit logging to patients table |

---

## 🔍 Sample Queries

```sql
-- View patient prescription history
SELECT * FROM GetPatientPrescriptions(1);

-- See upcoming appointments
SELECT * FROM GetPatientAppointments(1);

-- Audit log (after updating a patient)
SELECT * FROM patient_audit_log ORDER BY changed_at DESC;
```

---

## 📸 Screenshots

_Add screenshots from pgAdmin or VS Code here showing successful query results and table views._

---

## 👨‍💻 Author

**Gibson N. (DBA-GibsonN)**  
📧 [nwagboniwe.gibson@yahoo.com]  
🔗 https://github.com/DBA-GibsonN

---

## 📝 License

MIT License (or specify if different)
