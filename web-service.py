# Import libraries.
# for web service
from flask import Flask, request, jsonify, render_template
from flask_cors import cross_origin, CORS
# to load out trained model
from tensorflow.keras.models import load_model

# Create flask app and enable cors.
# A Flask extension for handling Cross Origin Resource Sharing (CORS), making cross-origin AJAX possible.
app = Flask(__name__)
cors = CORS(app)

# Load our machine learning model.
model = load_model('model.h5')

# To accept POST requests containing speed as an object, create a REST endpoint. 
# It is the duty of this REST endpoint to make predictions for given speeds.
@app.route('/predict', methods=['POST'])

# This function this method gets executed whenever a request is received at http://localhost:5000/predict endpoint.
def predict():
    # Get speed from request body and cast it to float.
    speed = float(request.json['speed'])
    # Predict the power up to 3 decimal plates using deep learning model for the received speed.
    prediction = round(model.predict([speed])[0][0], 3)
    # Return the speed and predicted power as JSON response.
    return jsonify({
        'speed': speed,
        'power': prediction
    })

# For rendering HTML templates
@app.route('/')
# This function gets executed whenever a request is received at http://:127.0.0.1:5000 endpoint.
def index():
    # Render the index.html template.
    return render_template('index.html')


# Main function to start app.
if __name__ == '__main__':
    # Run app.
    app.run()