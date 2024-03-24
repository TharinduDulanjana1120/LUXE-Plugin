# Import necessary libraries
from flask import Flask, render_template, request
import math
import os
from glob import glob


# Import the predict Blueprint
from predict import predict_blueprint

# Create a Flask application
app = Flask(__name__, template_folder='templates')

# Register the predict Blueprint
app.register_blueprint(predict_blueprint)

# Define the route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    # Check if the form is submitted
    if request.method == 'POST':
        # Get user input from the form
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        gender = request.form['gender']

        # Calculate Body Surface Area (BSA)
        bsa = math.sqrt((height * weight) / 3600)
        
        # Determine the result based on gender and BSA
        if (gender == 'male' and bsa < 1.70) or (gender == 'female' and bsa < 1.60):
            result = 'Small (S)'
        elif(gender == 'male' and 1.70 <= bsa < 1.90 ) or (gender == 'female' and 1.60 <= bsa < 1.80 ):
            result = 'Medium(M)'
        elif(gender == 'male' and 1.90 <= bsa < 2.10 ) or (gender == 'female' and 1.80 <= bsa < 2.00 ):
            result = 'Large(L)'
        elif(gender == 'male' and 2.10 <= bsa <= 2.30 ) or (gender == 'female' and 2.00 <= bsa < 2.20 ):
            result = 'Extra Large(XL)'
        elif(gender == 'male' and 2.30 <= bsa ) or (gender == 'female' and 2.20 <= bsa  ):
            result = ' Double Extra Large(XL)'
        else:
            result = 'Wrong inputs'

    # Render the HTML template with the result
    return render_template('index.html', result=result)

# Define route for bodyType.html
@app.route('/body-type')
def body_type():
    return render_template('BodyType.html')

# Define route for suggest.html
@app.route('/suggest')
def suggest():
    return render_template('suggest.html')

# Define route for suggest.html
@app.route('/testfile', methods=['POST'])
def testroute():
    gender = request.form['gender']
    skin_color = request.form['skinColor']
    occasion = request.form['occasion']
    body_type = request.form['bodyType']
    size = request.form['size']

    # Get the list of image files in the folder
    image_folder = 'static/images/female'  # Path to the folder containing images
    image_files = os.listdir(image_folder)
    
    image_folder_male = 'static/images/male'  # Path to the folder containing images
    image_files_male = os.listdir(image_folder_male)

    return render_template('test.html', gender=gender, skin_color=skin_color, occasion=occasion, body_type=body_type, size=size,image_files=image_files,image_files_male=image_files_male)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
