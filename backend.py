from flask import Flask, jsonify
from flask_cors import CORS
import random
import string
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Define a sample endpoint
@app.route('/api/generate', methods=['GET'])
def hello():
    print("Generating........")
    characters = string.ascii_letters + string.digits + string.punctuation
    length = 12
    # Ensure the password contains at least one of each type of character
    password = (
        random.choice(string.ascii_uppercase) +
        random.choice(string.ascii_lowercase) +
        random.choice(string.digits) +
        random.choice(string.punctuation)
    )

    # Generate the remaining characters randomly
    password += ''.join(random.choice(characters) for _ in range(length - len(password)))

    # Shuffle the characters to make the password more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return jsonify({'password': password})

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
