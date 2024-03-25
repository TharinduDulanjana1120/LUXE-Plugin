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



# Define the route for login.html
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/size')
def show_size():
    return render_template('size.html')

@app.route('/lo')

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
    image_folder = 'static/images/dp'  # Path to the folder containing images
    image_files = os.listdir(image_folder)

    image_folder2 = 'static/images/dc'  # Path to the folder containing images
    image_files2 = os.listdir(image_folder2)

    image_folder3 = 'static/images/df'  # Path to the folder containing images
    image_files3 = os.listdir(image_folder3)

    image_folder4 = 'static/images/np'  # Path to the folder containing images
    image_files4 = os.listdir(image_folder4)

    image_folder5 = 'static/images/nc'  # Path to the folder containing images
    image_files5 = os.listdir(image_folder5)

    image_folder6 = 'static/images/nf'  # Path to the folder containing images
    image_files6 = os.listdir(image_folder6)

    image_folder7 = 'static/images/mp'  # Path to the folder containing images
    image_files7 = os.listdir(image_folder7)

    image_folder8 = 'static/images/mc'  # Path to the folder containing images
    image_files8 = os.listdir(image_folder8)

    image_folder9 = 'static/images/mf'  # Path to the folder containing images
    image_files9 = os.listdir(image_folder9)

    image_folder10 = 'static/images/tp'  # Path to the folder containing images
    image_files10 = os.listdir(image_folder10)

    image_folder11 = 'static/images/tc'  # Path to the folder containing images
    image_files11 = os.listdir(image_folder11)

    image_folder12 = 'static/images/tf'  # Path to the folder containing images
    image_files12 = os.listdir(image_folder12)

    image_folder13 = 'static/images/wp'  # Path to the folder containing images
    image_files13 = os.listdir(image_folder13)

    image_folder14 = 'static/images/wc'  # Path to the folder containing images
    image_files14 = os.listdir(image_folder14)

    image_folder15 = 'static/images/wf'  # Path to the folder containing images
    image_files15 = os.listdir(image_folder15)
    
    # image_folder_male = 'static/images/male'  # Path to the folder containing images
    # image_files_male = os.listdir(image_folder_male)

    return render_template('test.html', gender=gender, skin_color=skin_color, occasion=occasion, body_type=body_type, size=size,image_files=image_files,image_files2=image_files2,image_files3=image_files3,image_files4=image_files4,image_files5=image_files5,image_files6=image_files6,image_files7=image_files7,image_files8=image_files8,image_files9=image_files9,image_files10=image_files10,image_files11=image_files11,image_files12=image_files12,image_files13=image_files13,image_files14=image_files14,image_files15=image_files15)


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
