# app.py
from flask import Flask, request, jsonify
import os
from dotenv import load_dotenv
from db import get_db_connection  # ✅ Use the centralized db function

# ✅ Load environment variables
load_dotenv()

app = Flask(__name__)

# ✅ Home route
@app.route('/')
def home():
    return jsonify({"message": "Hospital Management API is running"})


# ✅ POST: Add a new patient
@app.route('/patients', methods=['POST'])
def add_patient():
    data = request.get_json()

    required_fields = ['first_name', 'last_name', 'dob', 'gender', 'contact_info']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields in request body'}), 400

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO Patients (FirstName, LastName, DOB, Gender, ContactInfo)
            VALUES (%s, %s, %s, %s, %s)
        """, (
            data['first_name'],
            data['last_name'],
            data['dob'],
            data['gender'],
            data['contact_info']
        ))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Patient added successfully'}), 201

    except Exception as e:
        print(f"❌ ERROR: {e}")
        return jsonify({'error': str(e)}), 500


# ✅ GET: All patients
@app.route('/patients', methods=['GET'])
def get_patients():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Patients ORDER BY PatientID;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        patients = []
        for row in rows:
            patients.append({
                "PatientID": row[0],
                "FirstName": row[1],
                "LastName": row[2],
                "DOB": str(row[3]) if row[3] else None,
                "Gender": row[4],
                "ContactInfo": row[5]
            })

        return jsonify(patients)
    except Exception as e:
        print(f"❌ ERROR in GET /patients: {e}")
        return jsonify({'error': str(e)}), 500


# ✅ GET: Patient by ID
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT * FROM Patients WHERE PatientID = %s;', (id,))
        row = cur.fetchone()
        cur.close()
        conn.close()

        if row:
            patient = {
                "PatientID": row[0],
                "FirstName": row[1],
                "LastName": row[2],
                "DOB": str(row[3]) if row[3] else None,
                "Gender": row[4],
                "ContactInfo": row[5]
            }
            return jsonify(patient)
        else:
            return jsonify({"error": "Patient not found"}), 404

    except Exception as e:
        print(f"❌ ERROR in GET /patients/<id>: {e}")
        return jsonify({'error': str(e)}), 500


# ✅ PUT: Update a patient
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    try:
        data = request.get_json()
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            '''UPDATE Patients
               SET FirstName = %s, LastName = %s, DOB = %s, Gender = %s, ContactInfo = %s
               WHERE PatientID = %s;''',
            (
                data.get('first_name'),
                data.get('last_name'),
                data.get('dob'),
                data.get('gender'),
                data.get('contact_info'),
                id
            )
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Patient updated"})

    except Exception as e:
        print(f"❌ ERROR in PUT /patients/<id>: {e}")
        return jsonify({'error': str(e)}), 500


# ✅ DELETE: Delete a patient
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM Patients WHERE PatientID = %s;', (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"message": "Patient deleted"})

    except Exception as e:
        print(f"❌ ERROR in DELETE /patients/<id>: {e}")
        return jsonify({'error': str(e)}), 500


# ✅ Run locally
if __name__ == '__main__':
    app.run(debug=True)



# Add New Doctor
@app.route('/doctors', methods=['POST'])
def add_doctor():
    data = request.get_json()
    required = ['FirstName', 'LastName']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing fields'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Doctors (FirstName, LastName, Specialty, ContactInfo)
        VALUES (%s, %s, %s, %s) RETURNING DoctorID;
    """, (
        data['FirstName'],
        data['LastName'],
        data.get('Specialty'),
        data.get('ContactInfo')
    ))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Doctor added', 'DoctorID': new_id}), 201


@app.route('/doctors', methods=['GET'])
def get_doctors():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Doctors ORDER BY DoctorID;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    doctors = []
    for row in rows:
        doctors.append({
            "DoctorID": row[0],
            "FirstName": row[1],
            "LastName": row[2],
            "Specialty": row[3],
            "ContactInfo": row[4]
        })

    return jsonify(doctors)


@app.route('/doctors/<int:id>', methods=['GET'])
def get_doctor(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Doctors WHERE DoctorID = %s;", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        doctor = {
            "DoctorID": row[0],
            "FirstName": row[1],
            "LastName": row[2],
            "Specialty": row[3],
            "ContactInfo": row[4]
        }
        return jsonify(doctor)
    else:
        return jsonify({'error': 'Doctor not found'}), 404


@app.route('/doctors/<int:id>', methods=['PUT'])
def update_doctor(id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Doctors
        SET FirstName = %s, LastName = %s, Specialty = %s, ContactInfo = %s
        WHERE DoctorID = %s;
    """, (
        data.get('FirstName'),
        data.get('LastName'),
        data.get('Specialty'),
        data.get('ContactInfo'),
        id
    ))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Doctor updated'})


@app.route('/doctors/<int:id>', methods=['DELETE'])
def delete_doctor(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Doctors WHERE DoctorID = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Doctor deleted'})



# Appointments
@app.route('/appointments', methods=['POST'])
def add_appointment():
    data = request.get_json()
    required = ['PatientID', 'DoctorID', 'AppointmentDate', 'AppointmentTime']
    if not all(field in data for field in required):
        return jsonify({'error': 'Missing required fields'}), 400

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO Appointments (PatientID, DoctorID, AppointmentDate, AppointmentTime, Purpose)
        VALUES (%s, %s, %s, %s, %s) RETURNING AppointmentID;
    """, (
        data['PatientID'],
        data['DoctorID'],
        data['AppointmentDate'],
        data['AppointmentTime'],
        data.get('Purpose')
    ))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Appointment created', 'AppointmentID': new_id}), 201


@app.route('/appointments', methods=['GET'])
def get_appointments():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Appointments ORDER BY AppointmentDate, AppointmentTime;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    appointments = []
    for row in rows:
        appointments.append({
            "AppointmentID": row[0],
            "PatientID": row[1],
            "DoctorID": row[2],
            "AppointmentDate": str(row[3]),
            "AppointmentTime": str(row[4]),
            "Purpose": row[5]
        })

    return jsonify(appointments)


@app.route('/appointments/<int:id>', methods=['GET'])
def get_appointment(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Appointments WHERE AppointmentID = %s;", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return jsonify({
            "AppointmentID": row[0],
            "PatientID": row[1],
            "DoctorID": row[2],
            "AppointmentDate": str(row[3]),
            "AppointmentTime": str(row[4]),
            "Purpose": row[5]
        })
    else:
        return jsonify({'error': 'Appointment not found'}), 404


@app.route('/appointments/<int:id>', methods=['PUT'])
def update_appointment(id):
    data = request.get_json()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        UPDATE Appointments
        SET PatientID = %s, DoctorID = %s, AppointmentDate = %s, AppointmentTime = %s, Purpose = %s
        WHERE AppointmentID = %s;
    """, (
        data.get('PatientID'),
        data.get('DoctorID'),
        data.get('AppointmentDate'),
        data.get('AppointmentTime'),
        data.get('Purpose'),
        id
    ))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Appointment updated'})


@app.route('/appointments/<int:id>', methods=['DELETE'])
def delete_appointment(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM Appointments WHERE AppointmentID = %s;", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'message': 'Appointment deleted'})
