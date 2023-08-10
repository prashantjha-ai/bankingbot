
from flask import Flask, render_template, request, session, redirect, url_for, flash

from bot.bot import BankingBot

app = Flask(__name__)
app.secret_key = "your_secret_key_here"  # A secret key is required for session
bot = BankingBot()

@app.route('/')
def home():
    session.clear()
    session['state'] = ''
    return render_template('index.html', response="Type your Username", chat_history=[])

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        session['customername'] = username
        is_valid = bot.validate_credentials(username, password)  # Assuming this method exists

        if is_valid:
            session['authenticated'] = True
            # Redirect to submit with a parameter to indicate successful login
            return redirect(url_for('submit', logged_in=True))
        else:
            flash('Invalid credentials. Please try again.')
            # return redirect(url_for('login'))
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    chat_history = session.get('chat_history', [])

    if request.args.get('logged_in'):
        chat_history.append("You have successfully logged in!")

    if request.method == 'POST':
        user_input = request.form['user_input'].strip()
        
        response = bot.process_input(user_input)
        if response == 'REDIRECT_TO_LOGIN' and not session.get('authenticated', False):
            return redirect(url_for('login'))
        
        chat_history += [user_input, response]

    session['chat_history'] = chat_history

    return render_template('index.html', response=None, chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)

