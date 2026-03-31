# backend/app.py

from flask import Flask, jsonify, request
from flask_cors import CORS
from emotion_text import detect_text_emotion   # ← NEW

app = Flask(__name__)
CORS(app)

# Health check
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "Server is running",
        "message": "Emotion Adaptive Storytelling Backend Ready!"
    })

# Start story
@app.route('/start', methods=['POST'])
def start_story():
    return jsonify({
        "status": "ok",
        "message": "Story started!",
        "scene": "intro"
    })

# Get next scene — NOW WITH REAL EMOTION DETECTION
@app.route('/next', methods=['POST'])
def next_scene():
    data = request.get_json()
    user_text = data.get('text', '')

    # ← Detect emotion from text
    emotion = detect_text_emotion(user_text)

    return jsonify({
        "status": "ok",
        "received_text": user_text,
        "emotion": emotion,              # ← REAL emotion now!
        "next_scene": "scene_1",         # placeholder — Step 3
        "story_text": "The journey begins..."  # placeholder — Step 3
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)