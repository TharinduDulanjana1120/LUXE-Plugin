# Import necessary libraries
from flask import Flask, render_template, request
import requests
import base64

# Initialize Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for image classification
@app.route('/classify', methods=['POST'])
def classify_image():
    # Get image data from the request
    image_data = request.files['image'].read()

    # Encode image data to base64
    encoded_image = base64.b64encode(image_data).decode('utf-8')

    # Prepare payload for POST request to the machine learning model
    payload = {
        'instances': [{
            'image_bytes': {
                'b64': encoded_image
            }
        }]
    }

    # Send POST request to the machine learning model
    response = requests.post('https://teachablemachine.withgoogle.com/models/blAMVc866/', json=payload)

    # Parse response JSON
    prediction = response.json()['predictions'][0]

    # Get class label and confidence score
    class_label = prediction['label']
    confidence_score = prediction['confidence']

    # Return result
    return render_template('result.html', class_label=class_label, confidence_score=confidence_score)

if __name__ == '__main__':
    app.run(debug=True)