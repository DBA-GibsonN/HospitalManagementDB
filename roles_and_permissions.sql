-- ============================================
-- Create Users
-- ============================================

-- Admin
CREATE ROLE admin_user WITH LOGIN PASSWORD 'Admin123!';
GRANT ALL PRIVILEGES ON DATABASE hospital_db TO admin_user;

-- Doctor
CREATE ROLE doctor_user WITH LOGIN PASSWORD 'Doctor123!';

-- Patient
CREATE ROLE patient_user WITH LOGIN PASSWORD 'Patient123!';


-- ============================================
-- Table-Level Permissions
-- ============================================

-- Doctor permissions
GRANT SELECT ON Patients TO doctor_user;
GRANT SELECT, INSERT ON Prescriptions TO doctor_user;
GRANT SELECT ON Appointments TO doctor_user;

-- Patient permissions (read-only on their data)
GRANT SELECT ON Patients TO patient_user;
GRANT SELECT ON Appointments TO patient_user;
GRANT SELECT ON Prescriptions TO patient_user;

-- (Optional) prevent patient_user from seeing all rows later via RLS


-- Read-only user (e.g. Analyst)
CREATE ROLE analyst WITH LOGIN PASSWORD 'AnalystPass123';
GRANT CONNECT ON DATABASE hospital_db TO analyst;
GRANT USAGE ON SCHEMA public TO analyst;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO analyst;


