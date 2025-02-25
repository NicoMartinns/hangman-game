import random
from flask import Flask, render_template, url_for, request, redirect, session

possible_words = ['frog','snake']

app = Flask(__name__)
app.secret_key = 'MOBA'

@app.route("/")
def home():
    if 'choice_word' not in session:
        session['choice_word'] = random.choice(possible_words)
        session['hidden_word'] = ['_'] * len(session['choice_word'])
        session['life'] = 6
        session['wrong_letters'] = []

    return render_template(
        "index.html"
        ,hidden_word=' '.join(session['hidden_word'])
        ,life=session['life']
        ,wrong_letters=' '.join(session['wrong_letters'])
    )

@app.route("/play", methods=["POST",])
def play():

    letter = request.form.get("letter","").lower()
    #find = []

    if letter in session['choice_word']:
        new_hidden = list(session['hidden_word'])
        for index, letters in enumerate(session['choice_word']):
            if letter == letters:
                new_hidden[index] = letter
        session['hidden_word'] = new_hidden
            
        if "_" not in session['hidden_word']:
            return redirect(url_for('winner'))
    else:
        session['life'] -= 1
        session['wrong_letters'] = list(session['wrong_letters']) + [letter]
        
        if session['life'] <= 0:
            return redirect(url_for('loser'))
    
    session.modified = True
    return redirect(url_for('home'))

@app.route("/winner")
def winner():
    return render_template(
        'winner.html'
        ,choice_word=session['choice_word'].upper()
    )

@app.route("/loser")
def loser():
    return render_template(
        'loser.html'
    )

@app.route("/play_again")
def play_again():
    session.clear()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)