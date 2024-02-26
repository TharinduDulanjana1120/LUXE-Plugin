from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/suggest-clothing', methods=['GET'])
def suggest_clothing():
    skin_color = request.args.get('skinColor')
    occasion = request.args.get('occasion')
    gender = request.args.get('gender')

    # Implement your clothing suggestion logic here based on skin_color, occasion, and gender
    suggestion = get_clothing_suggestion(skin_color, occasion, gender)

    return jsonify({"suggestion": suggestion})

def get_clothing_suggestion(skin_color, occasion, gender):
    # Replace this with your actual clothing suggestion logic
    # This is just a placeholder
    if gender == 'male':
        return 'T-shirt and jeans'
    elif gender == 'female':
        return 'Dress and heels'
    else:
        return 'Suggestion not available for this gender'

if __name__ == '__main__':
    app.run(debug=True)
