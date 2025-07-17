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
