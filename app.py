from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

compliments = [
    "You have a beautiful smile! 😊",
    "You light up my world like nobody else! ✨",
    "You're an amazing person inside and out! 💖",
    "I’m so lucky to have you! 🍀",
    "You make my heart happy! 💕"
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compliment')
def compliment():
    return jsonify({"compliment": random.choice(compliments)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
