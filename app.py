# Import the necessary modules
from flask import Flask, render_template, jsonify, request
import psycopg2

app = Flask(__name__)

# Replace the following with your PostgreSQL database details
db_params = {
    'dbname': 'api',
    'user': 'ox',
    'password': 'ox',
    'host': 'localhost',
    'port': '5432'
}

# Define your REST API routes
@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/add')
def create():
    return render_template('add.html')

@app.route('/users', methods=['GET'])
def get_data():
    # Connect to PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users ORDER BY id')
    data = cursor.fetchall()

    # Close database connection
    cursor.close()
    connection.close()

    # Convert data to JSON and return
    return jsonify(data)

# Define the route for updating data
@app.route('/users/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # Connect to PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Get data from the request
    data = request.json
    new_name = data.get('name')
    new_email = data.get('email')

    # Update data in the database
    cursor.execute('UPDATE users SET name = %s, email = %s WHERE id = %s', (new_name, new_email, data_id))
    connection.commit()

    # Close database connection
    cursor.close()
    connection.close()

    # Return updated data
    return jsonify({'message': 'Data updated successfully'})

# Define the route for creating data
@app.route('/users', methods=['POST'])
def create_data():
    # Connect to PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Get data from the request
    data = request.json
    new_name = data.get('newName')
    new_email = data.get('newEmail')

    # Update data in the database
    cursor.execute('INSERT INTO users (name, email) VALUES (%s, %s) RETURNING id', (new_name, new_email))
    new_data_id = cursor.fetchone()[0]
    connection.commit()

    # Close database connection
    cursor.close()
    connection.close()

    # Return created data
    return jsonify({'id': new_data_id, 'name': new_name, 'email': new_email})

if __name__ == '__main__':
    app.run(debug=True)
