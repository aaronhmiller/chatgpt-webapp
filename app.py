# Import the necessary modules
from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)

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
      return response.json()
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
        return response.text
    else:
        # Handle errors or unsuccessful responses
        return jsonify({'error': 'Failed to update user data'}), response.status_code


# Define the route for creating data
@app.route('/users', methods=['POST'])
def create_data():

    # URL of the RESTful API endpoint for creating a new user
    api_url = 'https://api.demojoyto.win/users'

    # Extract the data to be created from the incoming request
    user_data = request.json

    # Make a POST request to the RESTful API
    response = requests.post(api_url, json=user_data)

    # Check if the request was successful
    if response.status_code == 201:
        # Return the created user data response
        return response.text
    else:
        # Handle errors or unsuccessful responses
        return jsonify({'error': 'Failed to create new user'}), response.status_code

# Define the route for deleting data
@app.route('/users/<int:data_id>', methods=['DELETE'])
def delete_data(data_id):

    # URL of the RESTful API endpoint for deleting a user
    api_url = f'https://api.demojoyto.win/users/{data_id}'

    # Make a DELETE request to the RESTful API
    response = requests.delete(api_url)

    # Check if the request was successful
    if response.status_code == 200 or response.status_code == 204:
        # Return a success message
        return jsonify({'message': f'User with ID {data_id} deleted successfully'}), 200
    else:
        # Handle errors or unsuccessful responses
        return jsonify({'error': 'Failed to delete user'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
