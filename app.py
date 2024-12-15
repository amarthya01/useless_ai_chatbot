from flask import Flask, request, jsonify
from responses import get_response

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_reply = get_response()  # Get bot's response
    
    # Return the bot response first, followed by the user message
    return jsonify({
        "bot_response": bot_reply,  # Bot's response first
        "user_message": user_message  # User's message second
    })

if __name__ == '__main__':
    app.run(debug=True)
