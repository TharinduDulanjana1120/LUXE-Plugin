# Import necessary libraries
from flask import Flask, render_template, request
import math

# Create a Flask application
app = Flask(__name__,template_folder='C:\University\L5\SDGP\Github\LUXE-Plugin\Sample 01 - Size Predict')

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
        else:
            result = 'Not Small'

    # Render the HTML template with the result
    return render_template('index.html', result=result)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
