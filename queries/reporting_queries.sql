-- ===============================
-- Reporting Queries for Hospital DB
-- Author: DBA-GibsonN
-- ===============================

-- 1. List all appointments with doctor and patient names
SELECT 
    a.AppointmentID,
    a.AppointmentDate,
    a.Status,
    CONCAT(p.first_name, ' ', p.last_name) AS Patient,
    CONCAT(d.firstname, ' ', d.lastname) AS Doctor
FROM Appointments a
JOIN Patients p ON a.PatientID = p.PatientID
JOIN Doctors d ON a.DoctorID = d.DoctorID
ORDER BY a.AppointmentDate;

-- 2. Get the prescription history of a patient
SELECT 
    CONCAT(p.first_name, ' ', p.last_name) AS Patient,
    m.MedicationName,
    pr.DatePrescribed,
    pr.DosageInstructions,
    CONCAT(d.firstname, ' ', d.lastname) AS PrescribingDoctor
FROM Prescriptions pr
JOIN Patients p ON pr.PatientID = p.PatientID
JOIN Medications m ON pr.MedicationID = m.MedicationID
JOIN Doctors d ON pr.DoctorID = d.DoctorID
WHERE p.first_name = 'Alice' AND p.last_name = 'Johnson';

-- 3. Count appointments by status
SELECT 
    Status,
    COUNT(*) AS Total
FROM Appointments
GROUP BY Status;

-- 4. List doctors and number of patients they have seen
SELECT 
    CONCAT(d.firstname, ' ', d.lastname) AS Doctor,
    COUNT(DISTINCT a.PatientID) AS PatientsSeen
FROM Doctors d
LEFT JOIN Appointments a ON d.DoctorID = a.DoctorID
GROUP BY d.firstname, d.lastname
ORDER BY PatientsSeen DESC;
