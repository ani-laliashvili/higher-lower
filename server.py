from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def guess_number():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src=https://media1.giphy.com/media/l378khQxt68syiWJy/giphy.gif?cid=ecf05e47ngpgnh9yssdmczz26nbn82f651pcm9qwg9orjvqd&rid=giphy.gif&ct=g>'

@app.route('/<int:guess>')
def check_guess(guess):
    if guess == number:
        return '<h1>You found me!</h1>' \
               '<img src=https://media2.giphy.com/media/TdfyKrN7HGTIY/giphy.gif?cid=ecf05e47bpl36x9ceghx2smrz7nxh58x2jamjhfi9ncj5ec6&rid=giphy.gif&ct=g>'
    elif guess < number:
        return '<h1>Too low, try again!</h1>' \
               '<img src=https://media3.giphy.com/media/ISOckXUybVfQ4/giphy.gif?cid=ecf05e473o4kzra63uif3zqkaj3c434vs1gze8gm63xayj87&rid=giphy.gif&ct=g>'
    else:
        return '<h1>Too high, try again!</h1>' \
               '<img src=https://media4.giphy.com/media/NTY1kHmcLsCsg/giphy.gif?cid=ecf05e473o4kzra63uif3zqkaj3c434vs1gze8gm63xayj87&rid=giphy.gif&ct=g>'

if __name__ == '__main__':
    number = random.randint(0, 9)

    app.run(debug=True)
