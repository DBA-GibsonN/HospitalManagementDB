-- ===============================
-- Reporting Queries for Hospital DB
-- ===============================

-- 1. List all appointments with doctor and patient names
SELECT 
    a.AppointmentID,
    a.AppointmentDate,
    a.Status,
    p.FullName AS Patient,
    d.FullName AS Doctor
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID
ORDER BY a.AppointmentDate;

-- 2. Get the prescription history of a patient
SELECT 
    p.FullName AS Patient,
    m.MedicationName,
    pr.DatePrescribed,
    pr.DosageInstructions
FROM Prescriptions pr
JOIN Patients p ON pr.PatientID = p.PatientID
JOIN Medications m ON pr.MedicationID = m.MedicationID
WHERE p.FullName = 'Alice Johnson';

-- 3. Count appointments by status
SELECT 
    Status,
    COUNT(*) AS Total
FROM Appointments
GROUP BY Status;

-- 4. List doctors and number of patients they have seen
SELECT 
    d.FullName AS Doctor,
    COUNT(DISTINCT a.PatientID) AS PatientsSeen
FROM Doctors d
LEFT JOIN Appointments a ON d.DoctorID = a.DoctorID
GROUP BY d.FullName
ORDER BY PatientsSeen DESC;
