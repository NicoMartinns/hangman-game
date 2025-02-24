import random
from flask import Flask, render_template, url_for, request, redirect

possible_words = ['frog','snake']
choice_word = random.choice(possible_words)
hidden_word = ['_'] * len(choice_word)
life = 6
wrong_letters = []

app = Flask(__name__)

@app.route("/")
def home():
    return render_template(
        "index.html"
        , hidden_word=' '.join(hidden_word)
        ,life=life
        ,wrong_letters=' '.join(wrong_letters)
    )

@app.route("/play", methods=["POST",])
def play():
    global hidden_word, life, choice_word,wrong_letters

    letter = request.form.get("letter").lower()
    find = []


    if letter in choice_word:
        for index, letters in enumerate(choice_word):
            if letter == letters:
                find.append((index,letters))
        
        for index, letters in find:
            hidden_word[index] = letter
            
        if "_" not in hidden_word:
            return redirect(url_for('winner'))
    else:
        life -= 1
        wrong_letters.append(letter)
        
        if life == 0:
            return redirect(url_for('loser'))
        
    return redirect(url_for('home'))

@app.route("/winner")
def winner():
    return render_template(
        'winner.html'
        ,choice_word=choice_word.upper()
    )

@app.route("/loser")
def loser():
    return render_template(
        'loser.html'
    )

if __name__ == '__main__':
    app.run(debug=True)