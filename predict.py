from flask import Blueprint, render_template, request

# Create a Blueprint for predict routes
predict_blueprint = Blueprint('predict', __name__)
a = ''
b = ''
c = ''
d = ''
e = ''
f = ''
g = ''
h = ''
i = ''

# @predict_blueprint.route('/suggest')
# def index():
#     return render_template('suggest.html')

@predict_blueprint.route('/suggest_clothing', methods=['POST'])
def suggest_clothing():
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i
    gender = request.form['gender']
    skin_color = request.form['skinColor']
    occasion = request.form['occasion']
    body_type = request.form['bodyType']
    size = request.form['size']
  
    suggestion = get_clothing_suggestion(gender, skin_color, occasion, body_type, size)

    return render_template('suggest.html', output=f'{suggestion}', image_path1 = a,image_path2 =b,image_path3 = c,image_path4 = d,image_path5 = e,image_path6 = f,image_path7 = g,image_path8 = h,image_path9 = i)

def get_clothing_suggestion(gender, skin_color, occasion, body_type, size):
    global a
    global b
    global c
    global d
    global e
    global f
    global g
    global h
    global i

    if gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        a = 'static\images\download.jpeg'
        b = 'static\images\F1.jpg'
        #return '1.1.1' , 'static/images/download.png'
        return a,b
    
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '1.1.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '1.1.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '1.1.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '1.1.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '1.2.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '1.2.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '1.2.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '1.2.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '1.2.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '1.3.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '1.3.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '1.3.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '1.3.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '1.3.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '1.4.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '1.4.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '1.4.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '1.4.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '1.4.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '1.5.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '1.5.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '1.5.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '1.5.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '1.5.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        return '2.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '2.1.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '2.1.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '2.1.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '2.1.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '2.2.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '2.2.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '2.2.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '2.2.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '2.2.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '2.3.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '2.3.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '2.3.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '2.3.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '2.3.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '2.4.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '2.4.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '2.4.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '2.4.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '2.4.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '2.5.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '2.5.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '2.5.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '2.5.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '2.5.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        return '3.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '3.1.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '3.1.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '3.1.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '3.1.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '3.2.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '3.2.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '3.2.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '3.2.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '3.2.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '3.3.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '3.3.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '3.3.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '3.3.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '3.3.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '3.4.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '3.4.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '3.4.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '3.4.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '3.4.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '3.5.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '3.5.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '3.5.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '3.5.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '3.5.5'
    
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '4.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '4.1.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '4.1.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '4.1.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '4.1.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '4.2.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '4.2.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '4.2.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '4.2.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '4.2.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '4.3.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '4.3.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '4.3.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '4.3.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '4.3.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '4.4.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '4.4.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '4.4.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '4.4.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '4.4.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '4.5.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '4.5.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        return '4.5.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '4.5.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '4.5.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '5.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '5.1.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '5.1.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '5.1.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '5.1.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '5.2.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '5.2.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '5.2.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '5.2.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '5.2.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '5.3.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '5.3.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '5.3.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '5.3.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '5.3.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '5.4.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '5.4.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '5.4.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '5.4.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '5.4.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '5.5.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '5.5.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        return '5.5.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '5.5.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '5.5.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '6.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '6.1.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '6.1.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '6.1.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '6.1.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '6.2.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '6.2.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '6.2.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '6.2.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '6.2.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '6.3.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '6.3.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '6.3.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '6.3.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '6.3.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '6.4.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '6.4.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '6.4.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '6.4.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '6.4.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '6.5.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '6.5.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        return '6.5.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '6.5.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '6.5.5'
    
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '7.1.1' , 'static\images\F1.jpg'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '7.1.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '7.1.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '7.1.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '7.1.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '7.2.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '7.2.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '7.2.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '7.2.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '7.2.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '7.3.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '7.3.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '7.3.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '7.3.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '7.3.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '7.4.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '7.4.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '7.4.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '7.4.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '7.4.5'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '7.5.1'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '7.5.2'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '7.5.3'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '7.5.4'
    elif gender == 'male' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '7.5.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '8.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '8.1.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '8.1.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '8.1.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '8.1.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '8.2.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '8.2.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '8.2.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '8.2.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '8.2.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '8.3.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '8.3.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '8.3.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '8.3.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '8.3.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '8.4.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '8.4.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '8.4.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '8.4.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '8.4.5'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '8.5.1'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '8.5.2'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '8.5.3'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '8.5.4'
    elif gender == 'male' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '8.5.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '9.1.1' , 'static/images/download.png'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '9.1.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '9.1.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '9.1.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '9.1.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '9.2.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '9.2.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '9.2.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '9.2.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '9.2.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '9.3.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '9.3.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '9.3.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '9.3.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '9.3.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '9.4.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '9.4.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '9.4.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '9.4.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '9.4.5'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '9.5.1'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '9.5.2'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '9.5.3'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '9.5.4'
    elif gender == 'male' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '9.5.5'
    
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        a = 'static\images\F1.jpg'
        b = ""
        # '1.1.1' , 'static/images/download.png'
        return a,b
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '1.1.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '1.1.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '1.1.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '1.1.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '1.2.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '1.2.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '1.2.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '1.2.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '1.2.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '1.3.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '1.3.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '1.3.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '1.3.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '1.3.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '1.4.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '1.4.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '1.4.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '1.4.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '1.4.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '1.5.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '1.5.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '1.5.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '1.5.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '1.5.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        return '2.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '2.1.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '2.1.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '2.1.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '2.1.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '2.2.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '2.2.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '2.2.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '2.2.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '2.2.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '2.3.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '2.3.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '2.3.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '2.3.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '2.3.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '2.4.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '2.4.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '2.4.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '2.4.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '2.4.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '2.5.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '2.5.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '2.5.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '2.5.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '2.5.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'small' :
        return '3.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'medium' :
        return '3.1.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'large' :
        return '3.1.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'extraLarge' :
        return '3.1.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '3.1.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'small' :
        return '3.2.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'medium' :
        return '3.2.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'large' :
        return '3.2.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'extraLarge' :
        return '3.2.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '3.2.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'small' :
        return '3.3.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'medium' :
        return '3.3.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'large' :
        return '3.3.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '3.3.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '3.3.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'small' :
        return '3.4.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'medium' :
        return '3.4.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'large' :
        return '3.4.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'extraLarge' :
        return '3.4.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '3.4.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'small' :
        return '3.5.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'medium' :
        return '3.5.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'large' :
        return '3.5.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'extraLarge' :
        return '3.5.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'fair' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '3.5.5'
    
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '4.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '4.1.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '4.1.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '4.1.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '4.1.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '4.2.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '4.2.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '4.2.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '4.2.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '4.2.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '4.3.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '4.3.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '4.3.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '4.3.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '4.3.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '4.4.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '4.4.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '4.4.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '4.4.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '4.4.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '4.5.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '4.5.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        return '4.5.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '4.5.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '4.5.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '5.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '5.1.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '5.1.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '5.1.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '5.1.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '5.2.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '5.2.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '5.2.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '5.2.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '5.2.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '5.3.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '5.3.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '5.3.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '5.3.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '5.3.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '5.4.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '5.4.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '5.4.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '5.4.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '5.4.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '5.5.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '5.5.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        return '5.5.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '5.5.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '5.5.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'small' :
        return '6.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'medium' :
        return '6.1.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'large' :
        return '6.1.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'extraLarge' :
        return '6.1.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '6.1.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'small' :
        return '6.2.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'medium' :
        return '6.2.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'large' :
        return '6.2.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'extraLarge' :
        return '6.2.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '6.2.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'small' :
        return '6.3.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'medium' :
        return '6.3.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'large' :
        return '6.3.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '6.3.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '6.3.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'small' :
        return '6.4.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'medium' :
        return '6.4.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'large' :
        return '6.4.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'extraLarge' :
        return '6.4.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '6.4.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'small' :
        return '6.5.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'medium' :
        return '6.5.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'large' :
        a = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p1.png'
        b = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p2.png'
        c = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p3.png'
        d = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p4.png'
        e = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p5.png'
        f = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p6.png'
        g = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p7.png'
        h = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p8.png'
        i = 'static\\images\\female-party-tan-invertedtriangle-large\\nihithi_p9.png'
        return a,b,c,d,e,f,g,h,i
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'extraLarge' :
        return '6.5.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'tan' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '6.5.5'
    
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '7.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '7.1.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '7.1.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '7.1.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '7.1.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '7.2.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '7.2.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '7.2.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '7.2.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '7.2.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '7.3.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '7.3.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '7.3.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '7.3.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '7.3.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '7.4.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '7.4.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '7.4.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '7.4.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '7.4.5'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '7.5.1'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '7.5.2'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '7.5.3'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '7.5.4'
    elif gender == 'female' and occasion == 'casual' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '7.5.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '8.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '8.1.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '8.1.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '8.1.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '8.1.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '8.2.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '8.2.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '8.2.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '8.2.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '8.2.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '8.3.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '8.3.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '8.3.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '8.3.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '8.3.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '8.4.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '8.4.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '8.4.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '8.4.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '8.4.5'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '8.5.1'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '8.5.2'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '8.5.3'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '8.5.4'
    elif gender == 'female' and occasion == 'formal' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '8.5.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'small' :
        return '9.1.1' , 'static/images/download.png'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'medium' :
        return '9.1.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'large' :
        return '9.1.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'extraLarge' :
        return '9.1.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'pear' and size == 'doubleExtraLarge' :
        return '9.1.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'small' :
        return '9.2.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'medium' :
        return '9.2.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'large' :
        return '9.2.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'extraLarge' :
        return '9.2.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'rectangle' and size == 'doubleExtraLarge' :
        return '9.2.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'small' :
        return '9.3.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'medium' :
        return '9.3.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'large' :
        return '9.3.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'extraLarge' :
        return '9.3.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'invertedTriangle' and size == 'doubleExtraLarge' :
        return '9.3.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'small' :
        return '9.4.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'medium' :
        return '9.4.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'large' :
        return '9.4.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'extraLarge' :
        return '9.4.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'oval' and size == 'doubleExtraLarge' :
        return '9.4.5'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'small' :
        return '9.5.1'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'medium' :
        return '9.5.2'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'large' :
        return '9.5.3'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'extraLarge' :
        return '9.5.4'
    elif gender == 'female' and occasion == 'party' and skin_color == 'dark' and body_type == 'slim' and size == 'doubleExtraLarge' :
        return '9.5.5'
    else:
        return 'No products in this moment for your preferences'
