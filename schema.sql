-- ===============================
-- Hospital Management Database Schema
-- Author: Gibson (DBA-GibsonN)
-- ===============================

-- Create Patients table
CREATE TABLE Patients (
    PatientID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DOB DATE,
    Gender VARCHAR(10),
    ContactInfo VARCHAR(100)
);

-- Create Doctors table
CREATE TABLE Doctors (
    DoctorID SERIAL PRIMARY KEY,
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    Specialty VARCHAR(50),
    DepartmentID INT
);

-- Create Departments table
CREATE TABLE Departments (
    DepartmentID SERIAL PRIMARY KEY,
    DepartmentName VARCHAR(100) NOT NULL
);

-- Create Appointments table
CREATE TABLE Appointments (
    AppointmentID SERIAL PRIMARY KEY,
    PatientID INT REFERENCES Patients(PatientID),
    DoctorID INT REFERENCES Doctors(DoctorID),
    AppointmentDate TIMESTAMP,
    Status VARCHAR(20)
);

-- Create Medications table
CREATE TABLE Medications (
    MedicationID SERIAL PRIMARY KEY,
    MedicationName VARCHAR(100),
    Dosage VARCHAR(50)
);

-- Create Prescriptions table
CREATE TABLE Prescriptions (
    PrescriptionID SERIAL PRIMARY KEY,
    PatientID INT REFERENCES Patients(PatientID),
    DoctorID INT REFERENCES Doctors(DoctorID),
    MedicationID INT REFERENCES Medications(MedicationID),
    AppointmentID INT REFERENCES Appointments(AppointmentID),
    DosageInstructions TEXT,
    DatePrescribed DATE
);
