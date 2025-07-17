-- ========================================
-- Audit Log Table for Patient Changes
-- ========================================

CREATE TABLE patient_audit_log (
    audit_id SERIAL PRIMARY KEY,
    operation_type TEXT NOT NULL,
    patient_id INT,
    changed_by TEXT,
    change_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    old_data JSONB,
    new_data JSONB
);


-- ========================================
-- Trigger Function to Log Changes
-- ========================================

CREATE OR REPLACE FUNCTION log_patient_changes()
RETURNS TRIGGER AS $$
BEGIN
    IF TG_OP = 'INSERT' THEN
        INSERT INTO patient_audit_log(operation_type, patient_id, changed_by, new_data)
        VALUES ('INSERT', NEW.patient_id, current_user, to_jsonb(NEW));
        RETURN NEW;

    ELSIF TG_OP = 'UPDATE' THEN
        INSERT INTO patient_audit_log(operation_type, patient_id, changed_by, old_data, new_data)
        VALUES ('UPDATE', NEW.patient_id, current_user, to_jsonb(OLD), to_jsonb(NEW));
        RETURN NEW;

    ELSIF TG_OP = 'DELETE' THEN
        INSERT INTO patient_audit_log(operation_type, patient_id, changed_by, old_data)
        VALUES ('DELETE', OLD.patient_id, current_user, to_jsonb(OLD));
        RETURN OLD;
    END IF;
END;
$$ LANGUAGE plpgsql;


-- ========================================
-- Attach Trigger to the Patients Table
-- ========================================

DROP TRIGGER IF EXISTS patient_audit_trigger ON patients;

CREATE TRIGGER patient_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON patients
FOR EACH ROW
EXECUTE FUNCTION log_patient_changes();


-- ========================================
-- Attach Trigger to the Patients Table
-- ========================================

DROP TRIGGER IF EXISTS patient_audit_trigger ON patients;

CREATE TRIGGER patient_audit_trigger
AFTER INSERT OR UPDATE OR DELETE ON patients
FOR EACH ROW
EXECUTE FUNCTION log_patient_changes();
