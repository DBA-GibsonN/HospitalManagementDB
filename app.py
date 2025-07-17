from flask import Flask, request, jsonify
import psycopg2
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

# PostgreSQL connection setup
def get_db_connection():
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT")
    )
    return conn

# CREATE
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
        """, (data['first_name'], data['last_name'], data['dob'], data['gender'], data['contact_info']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Patient added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# READ (All)
@app.route('/patients', methods=['GET'])
def get_patients():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patients")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    patients = [{
        'id': row[0],
        'first_name': row[1],
        'last_name': row[2],
        'dob': row[3],
        'gender': row[4],
        'contact_info': row[5]
    } for row in rows]

    return jsonify(patients)

# READ (One)
@app.route('/patients/<int:id>', methods=['GET'])
def get_patient(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Patients WHERE PatientID = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return jsonify({
            'id': row[0],
            'first_name': row[1],
            'last_name': row[2],
            'dob': row[3],
            'gender': row[4],
            'contact_info': row[5]
        })
    else:
        return jsonify({'error': 'Patient not found'}), 404

# UPDATE
@app.route('/patients/<int:id>', methods=['PUT'])
def update_patient(id):
    data = request.get_json()
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Patients
            SET FirstName = %s, LastName = %s, DOB = %s, Gender = %s, ContactInfo = %s
            WHERE PatientID = %s
        """, (data['first_name'], data['last_name'], data['dob'], data['gender'], data['contact_info'], id))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Patient updated successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# DELETE
@app.route('/patients/<int:id>', methods=['DELETE'])
def delete_patient(id):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("DELETE FROM Patients WHERE PatientID = %s", (id,))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'message': 'Patient deleted successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
