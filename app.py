from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

compliments = [
    "You have a beautiful smile! 😊",
    "You light up my world like nobody else! ✨",
    "You're an amazing person inside and out! 💖",
    "I’m so lucky to have you! 🍀",
    "You make my heart happy! 💕",
    "You bring so much joy into my life! 😊",
    "Your kindness is like a warm hug! 🤗",
    "You’re more beautiful than the stars! 🌟",
    "You have the best sense of humor! 😂",
    "You’re a shining light in my life! 🌟",
    "You make everything better just by being you! 🌸",
    "Your heart is as big as the universe! 💫",
    "I feel so lucky to know you! 🍀",
    "Your energy is contagious in the best way! ⚡",
    "You are loved more than words can say! ❤️",
    "You make the world a better place just by existing! 🌍",
    "You’re like sunshine on a rainy day! ☀️",
    "You are the best thing that ever happened to me! 💝",
    "You make life so much sweeter! 🍯",
    "You are absolutely stunning inside and out! 😍",
    "I appreciate you more than you’ll ever know! 🥰",
    "You inspire me every day! ✨",
    "You bring peace and calm wherever you go. 🌸",
    "Your heart is as beautiful as your soul! 💖",
    "Your laughter is the best sound in the world! 🎶",
    "I admire your strength and resilience! 💪",
    "You make everything feel possible! 🌈",
    "You light up every room you enter! 🌟",
    "Your positivity is so uplifting! 💫",
    "You are a true gift to the world! 🎁",
    "You are so unique and special! 💎",
    "Your presence is a gift to everyone around you! 🎁",
    "You make life feel like a dream come true! 🌙",
    "Your warmth and kindness are unmatched! 💖",
    "You have an amazing way of making others feel special! 🥰",
    "Your creativity knows no bounds! 🎨",
    "You bring so much light into this world! 🌞",
    "You are simply radiant! ✨",
    "Your strength and grace inspire me! 🌟",
    "You make every moment magical! ✨",
    "You’re a true gem in this world! 💎",
    "I’m always so happy when I see you! 😊",
    "Your soul shines brighter than the stars! 🌠",
    "You have a heart full of love! 💖",
    "You make everything more colorful! 🌈",
    "You have a gift for making people feel welcome! 🌸",
    "You are the most precious person I know! 🌹",
    "You have a heart that’s pure and kind! 💓",
    "You are a ray of sunshine in this world! 🌞",
    "You’re one in a million! 💖",
    "You are an absolute treasure! 💎",
    "You brighten everyone’s day just by being yourself! 🌞",
    "You are simply amazing in every way! 🌟",
    "Your heart is as beautiful as your smile! 😁",
    "You’re a blessing to everyone who knows you! 🙏",
    "You bring magic wherever you go! 🧚‍♀️",
    "You are beautiful, inside and out! 🌹",
    "You have the ability to make the world feel brighter! 🌞"
]


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compliment')
def compliment():
    return jsonify({"compliment": random.choice(compliments)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
