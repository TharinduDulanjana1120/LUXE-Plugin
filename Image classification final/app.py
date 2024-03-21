from flask import Flask, render_template, request, jsonify
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

app = Flask(__name__)

# Class labels
class_labels = ["Rectangle", "Pear", "Inverted Triangle", "Oval", "Slim", "Not Human"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Load model
    model = tensorflow.keras.models.load_model('keras_model.h5')

    # Process image
    image = Image.open(request.files['file'])
    image = ImageOps.fit(image, (224, 224), Image.ANTIALIAS)
    image = np.array(image)
    image = image.reshape(-1, 224, 224, 3)

    # Make prediction
    prediction = model.predict(image)
    result = np.argmax(prediction[0])

    # Get class label
    class_label = class_labels[result]

    # Return prediction result
    return jsonify({'result': class_label})

if __name__ == '__main__':
    app.run(debug=True)