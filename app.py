# Import the necessary modules
from flask import Flask, render_template, jsonify, request
import psycopg2
import requests

app = Flask(__name__)

# Replace the following with your PostgreSQL database details
# NOTE: use localhost if running outside docker compose
db_params = {
    'dbname': 'api',
    'user': 'ox',
    'password': 'ox',
    'host': 'postgres',
#    'host': 'localhost',
    'port': '5432'
}

# Define a default route
@app.route('/')
def index():
    return render_template('update.html')

# Define your REST API routes
@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/add')
def create():
    return render_template('add.html')

@app.route('/delete')
def delete():
    return render_template('delete.html')

@app.route('/users', methods=['GET'])
def get_data():
    # URL of the RESTful API endpoint
    api_url = 'https://api.demojoyto.win/users'

    # Make a GET request to the RESTful API
    response = requests.get(api_url)

    # Check if the request was successful
    if response.status_code == 200:
      # Convert the response to JSON
      data = response.json()
      return jsonify(data)
    else:
      # Handle errors or unsuccessful responses
      return jsonify({'error': 'Failed to fetch data from API'}), response.status_code

# Define the route for updating data
@app.route('/users/<int:data_id>', methods=['PUT'])
def update_data(data_id):
    # URL of the RESTful API endpoint
    api_url = f'https://api.demojoyto.win/users/{data_id}'

    # Get data from the request
    data = request.json

    # Make a PUT request to the RESTful API
    response = requests.put(api_url, json=data)

    # Check if the request was successful
    if response.status_code == 200:
        # Return the updated user data
        return response.json()
    else:
        # Handle errors or unsuccessful responses
        return jsonify({'error': 'Failed to update user data'}), response.status_code


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

# Define the route for deleting data
@app.route('/users/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):
    # Connect to PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Delete data from the database
    cursor.execute('DELETE FROM users WHERE id = %s', [data_id])
    connection.commit()

    # Close database connection
    cursor.close()
    connection.close()

    # Return a response
    return jsonify({'message': f'Data with ID {data_id} deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
