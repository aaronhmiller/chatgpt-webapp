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
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users', methods=['GET'])
def get_data():
    # Connect to PostgreSQL database
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Replace 'your_table_name' with your actual table name
    cursor.execute('SELECT * FROM users')
    data = cursor.fetchall()

    # Close database connection
    cursor.close()
    connection.close()

    # Convert data to JSON and return
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

