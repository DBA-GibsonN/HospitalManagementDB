from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Database config from .env
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

# Function to connect to the database
def get_db_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

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


# ✅ PUT: Update a patient
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
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


# ✅ DELETE: Delete a patient
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM Patients WHERE PatientID = %s;', (id,))
    conn.commit()
    cur.close()
    conn.close()

    return jsonify({"message": "Patient deleted"})


# ✅ Run locally if needed
if __name__ == '__main__':
    app.run(debug=True)
