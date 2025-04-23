from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_input = request.args.get('msg')  # Get user input
    return jsonify({"response": get_response(user_input)})  # Send chatbot response

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Make sure this is in your script, not in the terminal
