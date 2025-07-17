-- Get a patient's appointment history
CREATE OR REPLACE FUNCTION GetPatientAppointments(pid INT)
RETURNS TABLE (
    AppointmentID INT,
    AppointmentDate TIMESTAMP,
    Status VARCHAR,
    DoctorName VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        a.AppointmentID,
        a.AppointmentDate,
        a.Status,
        d.FullName AS DoctorName
    FROM Appointments a
    JOIN Doctors d ON a.DoctorID = d.DoctorID
    WHERE a.PatientID = pid;
END;
$$ LANGUAGE plpgsql;


-- ============================================
-- Function: GetPatientPrescriptions
-- Description: Returns a patient's prescription history
-- ============================================

CREATE OR REPLACE FUNCTION GetPatientPrescriptions(pid INT)
RETURNS TABLE (
    MedicationName VARCHAR,
    DosageInstructions TEXT,
    DatePrescribed DATE,
    DoctorName VARCHAR
) AS $$
BEGIN
    RETURN QUERY
    SELECT 
        m.MedicationName,
        pr.DosageInstructions,
        pr.DatePrescribed,
        d.FullName AS DoctorName
    FROM Prescriptions pr
    JOIN Medications m ON pr.MedicationID = m.MedicationID
    JOIN Doctors d ON pr.DoctorID = d.DoctorID
    WHERE pr.PatientID = pid;
END;
$$ LANGUAGE plpgsql;
