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
