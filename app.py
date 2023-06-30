from flask import Flask, render_template, request
from bot.bot import BankingBot


app = Flask(__name__)
bot = BankingBot()


@app.route('/')
def home():
    chat_history = []  # Initialize an empty chat history
    response = "Hello! How can I assist you today?"  # Welcome message
    return render_template('index.html', response=response, chat_history=chat_history)


@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']
    chat_history_str = request.form.get('chat_history', '[]')
    chat_history = eval(chat_history_str)

    response = bot.process_input(user_input)
    chat_history.append(user_input)
    chat_history.append(response)

    return render_template('index.html', response=response, chat_history=chat_history)


if __name__ == '__main__':
    app.run(debug=True)
