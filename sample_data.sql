-- ===============================
-- Sample Data for Hospital DB
-- ===============================

-- Departments
INSERT INTO Departments (DepartmentName) VALUES
('Cardiology'), ('Pediatrics'), ('Neurology'), ('Oncology');

-- Doctors
INSERT INTO Doctors (FullName, Specialty, DepartmentID) VALUES
('Dr. Linda Carter', 'Cardiologist', 1),
('Dr. John Smith', 'Pediatrician', 2),
('Dr. Emily Stone', 'Neurologist', 3),
('Dr. Omar Malik', 'Oncologist', 4);

-- Patients
INSERT INTO Patients (FullName, DOB, Gender, ContactInfo) VALUES
('Alice Johnson', '1990-04-12', 'Female', 'alice.johnson@example.com'),
('Michael Brown', '1985-11-23', 'Male', 'michael.brown@example.com'),
('Sofia Ramirez', '2002-07-05', 'Female', 'sofia.ramirez@example.com');

-- Medications
INSERT INTO Medications (MedicationName, Dosage) VALUES
('Atorvastatin', '10mg daily'),
('Paracetamol', '500mg twice a day'),
('Ibuprofen', '400mg as needed');

-- Appointments
INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, Status) VALUES
(1, 1, '2025-07-18 10:30:00', 'Scheduled'),
(2, 2, '2025-07-18 11:00:00', 'Completed'),
(3, 3, '2025-07-19 14:00:00', 'Cancelled');

-- Prescriptions
INSERT INTO Prescriptions (PatientID, DoctorID, MedicationID, AppointmentID, DosageInstructions, DatePrescribed) VALUES
(1, 1, 1, 1, 'Take one tablet daily after meals', '2025-07-18'),
(2, 2, 2, 2, 'Take two tablets per day for 5 days', '2025-07-18');
